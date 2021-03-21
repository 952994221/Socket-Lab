import time

# args is: id, name, sex, age， path
def item_pack(*args):
    result = ""
    for s in args:
        result += str(s)
        result += " "
    return result[:-1]

# head_line is str
# header is dict
# data is list[item_str1, item_str2, ...]: ["id name sex age path", ...]
# msg is str
def msg_pack(head_line, header, data):
    msg = ""
    line = head_line + "\r\n"
    msg += line
    for key in header:
        line = str(key) + ": " + str(header[key]) + "\r\n"
        msg += line
    msg += "\r\n"
    for item in data:
        line = item + "\r\n"
        msg += line
    return msg

# return [head_line, header, data]
# head_line, header, data see above
# msg is str
def msg_unpack(msg):
    lines = msg.split("\r\n")
    head_line = lines[0]
    lines = lines[1:-1]
    is_header = True
    header = {}
    data = []
    for line in lines:
        if not line:
            is_header = False
            continue
        if is_header:
            words = line.split(": ")
            header[words[0]] = words[-1]
        else:
            data.append(line)
    return [head_line, header, data]

def gen_default_header():
    header = {}
    cur_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    header['Time'] = cur_time
    header['Version'] = 'MyProtocol 1.0'
    return header