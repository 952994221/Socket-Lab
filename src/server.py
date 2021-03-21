import StudentService
from StudentEntity import Student
import Protocol
import socket
import threading
import sys, os
import re

mylist = list()

cmd = ("SEARCH", "INSERT", "UPDATE", "DELETE")

# item is ["id", "name", "sex", "age"]
# rst is list[item_str1， item_str2, ...]
# 单步执行数据库操作
def sql_opt_once(cmd, item):
    rst = []
    if cmd=="SEARCH":
        if item[0]!="$": # 使用id搜索，只得到0或1条结果
            id = int(item[0])
            student = StudentService.search_by_id(id)
            if student:
                r = student.to_string()
                path = StudentService.search_img(id)
                if path and os.path.isfile(path):
                    r += " " + path
                else:
                    r += " $"
                rst.append(r)
            else:
                return False
        # 由于图片是用id标识的，这种方式找不到图片
        elif item[1]!="$" or item[2]!="$" or item[3]!="$": # 使用其他信息搜索，会得到0或多条结果
            students = StudentService.search_by_other_info(item[1], item[2], item[3])
            if students:
                for student in students:
                    r = student.to_string()
                    r += " $"
                    rst.append(r)
            else:
                return False
        else:
            return False
    elif cmd=="UPDATE":
        student = Student(int(item[0]), str(item[1]), int(item[2]), int(item[3]))
        rst = StudentService.update(student)
        if rst:
            return True
        else:
            return False
    elif cmd=="INSERT":
        student = Student(int(item[0]), str(item[1]), int(item[2]), int(item[3]))
        rst = StudentService.insert(student)
        if rst:
            return True
        else:
            return False
    elif cmd=="DELETE":
        if item[0]!="$":
            id = int(item[0])
            rst = StudentService.delete_by_id(id)
            # 删除图片出错不影响
            img_rst = StudentService.delete_img(id)
            if rst:
                return True
            else:
                return False
        else:
            return False
    else:
        return False
    return rst


# data is list[item_str1, item_str2, ...]
# item_str is "id name sex age"
# item is ["id", "name", "sex", "age"]
def handle_request(myconnection, head_line, header, data):
    shead_line = "200"
    sdata = []
    sheader = {}
    for item_str in data:
        item = item_str.split(" ")
        # rst is list[item_str]
        rst = sql_opt_once(head_line, item)
        if not rst:
            shead_line = "400"
            if item[0]!="$":
                sheader[item[0]] = "FAIL"
            continue
        else:
            if item[0]!="$":
                sheader[item[0]] = "SUCCESS"
        if type(rst)!=bool:
            for s in rst:
                sdata.append(s)
    
    sheader.update(Protocol.gen_default_header())
    smsg = Protocol.msg_pack(shead_line, sheader, sdata)
    myconnection.send(smsg.encode("unicode_escape"))
        
# 图片传输预处理，在服务器上创建文件，并发送信息给客户端
def preopt_image(myconnection, head_line, header, data):
    id = header["Image"]
    file_name = header["FileName"]
    file_size = header["FileSize"]
    path = os.getcwd() + "/" + id + "_" + file_name
    fp = open(path, "wb")
    fp.close()
    sheader = Protocol.gen_default_header()
    info = "Image_" + id
    sheader.update({info: "READY", "Path": path})
    smsg = Protocol.msg_pack("300", sheader, [])
    myconnection.send(smsg.encode("unicode_escape"))
    return path

def sub_thread_in(myconnection, connNumber):
    mylist.append(myconnection)
    while True:
        try:
            recvedMsg = myconnection.recv(1024)
            if recvedMsg:
                is_cmd = False
                for c in cmd:
                    if re.match(c.encode("unicode_escape"), recvedMsg):
                        is_cmd = True
                if is_cmd: # 文本信息
                    recvedMsg = recvedMsg.decode("unicode_escape")
                    print("receive from connection:", connNumber)
                    print(recvedMsg, end="")
                    rst = Protocol.msg_unpack(recvedMsg)
                    head_line = rst[0]
                    header = rst[1]
                    data = rst[2]
                    handle_request(myconnection, head_line, header, data)
                elif re.match("IMAGE".encode("unicode_escape"), recvedMsg): # 图片预处理
                    #print("image cmd")
                    recvedMsg = recvedMsg.decode("unicode_escape")
                    print("receive from connection:", connNumber)
                    print(recvedMsg, end="")
                    rst = Protocol.msg_unpack(recvedMsg)
                    head_line = rst[0]
                    header = rst[1]
                    data = rst[2]
                    img_path = preopt_image(myconnection, head_line, header, data)
                    fp = open(img_path, "wb")
                else: # 图片传输
                    if os.path.isfile(img_path):
                        #print(img_path, " exist")
                        try:
                            if len(recvedMsg)==1024:
                                fp.write(recvedMsg)
                            else:
                                fp.write(recvedMsg)
                                fp.close()
                                id = header["Image"]
                                info = "Image_" + id
                                img_path = img_path.replace("\\","/") # windows的默认路径分隔符为"\","\"无法存入mysql
                                #print(img_path)
                                StudentService.insert_img(int(id), img_path)
                                sheader = Protocol.gen_default_header()
                                sheader.update({info: "SUCCESS"})
                                smsg = Protocol.msg_pack("300", sheader, [])
                                myconnection.send(smsg.encode("unicode_escape"))
                        except:
                            sheader = Protocol.gen_default_header()
                            id = header["Image"]
                            info = "Image_" + id
                            sheader.update({info: "FAIL"})
                            smsg = Protocol.msg_pack("500", sheader, [])
                            myconnection.send(smsg.encode("unicode_escape"))
        except:
        #except (OSError, ConnectionResetError):
            try:
                mylist.remove(myconnection)
            except:
                pass
            print(connNumber, 'exit, ', len(mylist), 'left')
            myconnection.close()
            return
 
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.bind(('localhost', 30000))

sock.listen(5)
print('Server', socket.gethostbyname('localhost'), 'listening ...')

while True:
    connection, addr = sock.accept()
    print('Accept a new connection', connection.getsockname(), connection.fileno())
    try:
        buf = connection.recv(1024).decode("unicode_escape")
        if buf == '1':
            connection.send(b'welcome to server!')
            mythread = threading.Thread(target=sub_thread_in, args=(connection, connection.fileno()))
            mythread.setDaemon(True)
            mythread.start() 
        else:
            connection.send(b'please go out!')
            connection.close()
    except:
        sys.exit(1)