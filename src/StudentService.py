# 数据库操作函数
from StudentEntity import Student
import MysqlUtils
import os

def insert(student):
    try:
        db = MysqlUtils.db
        cursor = db.cursor()
        id = student.get_id()
        name = student.get_name()
        sex = student.get_sex()
        age = student.get_age()
        sql = "insert into students value(%d, '%s', %d, %d)" % (id, name, sex, age)
        cursor.execute(sql)
        print("insert success")
        db.commit()
        return True
    except:
        db.rollback()
        print("insert failed")
        return False

def update(student):
    try:
        db = MysqlUtils.db
        cursor = db.cursor()
        id = student.get_id()
        name = student.get_name()
        sex = student.get_sex()
        age = student.get_age()
        sql = "update students set name='%s', sex=%d, age=%d where id=%d" % (name, sex, age, id)
        cursor.execute(sql)
        print("update success")
        db.commit()
        return True
    except:
        db.rollback()
        print("update failed")
        return False

def delete_by_id(id):
    try:
        db = MysqlUtils.db
        cursor = db.cursor()
        #print("delete", id)
        sql = "delete from students where id=%d" % id
        cursor.execute(sql)
        print("delete_by_id success")
        db.commit()
        return True
    except:
        db.rollback()
        print("delete_by_id failed")
        return False

# id is int
def search_by_id(id):
    try:
        db = MysqlUtils.db
        cursor = db.cursor()
        sql = "select * from students where id=%d" % id
        cursor.execute(sql)
        # fetchone return type is tuple
        result = cursor.fetchone()
        student = Student(int(result[0]), str(result[1]), int(result[2]), int(result[3]))
        print("search_by_id success")
        # return then goto finally
        return student
    except:
        # db.rollback()
        print("search_by_id failed")
        return False

# name, sex, age are str
def search_by_other_info(name, sex, age):
    students = []
    try:
        db = MysqlUtils.db
        cursor = db.cursor()
        if name!="$":
            sql = "select * from students where name='%s'" % str(name)
            cursor.execute(sql)
            results = cursor.fetchall()
            for result in results:
                if sex!="$" and sex!=result[2]:
                    continue
                if age!="$" and age!=result[3]:
                    continue
                student = Student(int(result[0]), str(result[1]), int(result[2]), int(result[3]))
                students.append(student)
        elif sex!="$":
            sql = "select * from students where sex=%d" % int(sex)
            cursor.execute(sql)
            results = cursor.fetchall()
            for result in results:
                if age!="$" and age!=result[3]:
                    continue
                student = Student(int(result[0]), str(result[1]), int(result[2]), int(result[3]))
                students.append(student)
        elif age!="$":
            sql = "select * from students where age=%d" % int(age)
            cursor.execute(sql)
            results = cursor.fetchall()
            for result in results:
                student = Student(int(result[0]), str(result[1]), int(result[2]), int(result[3]))
                students.append(student)
        else:
            print("search_by_other_info success")
            return False
        print("search_by_other_info success")
        return students
    except:
        print("search_by_other_info success")
        return False

def get_all_student():
    students = []
    try:
        db = MysqlUtils.db
        cursor = db.cursor()
        sql = "select * from students order by id"
        cursor.execute(sql)
        results = cursor.fetchall()
        for result in results:
            student = Student(int(result[0]), str(result[1]), int(result[2]), int(result[3]))
            students.append(student)
        print("get_all_student success")
        return students
    except:
        # db.rollback()
        print("get_all_student failed")
        return False

def insert_img(id, path):
    try:
        db = MysqlUtils.db
        cursor = db.cursor()
        sql = "insert into images value(%d, '%s')" % (id, path)
        cursor.execute(sql)
        print("insert_img success")
        db.commit()
        return True
    except:
        db.rollback()
        print("insert_img failed")
        return False

def search_img(id):
    try:
        db = MysqlUtils.db
        cursor = db.cursor()
        sql = "select image_path from images where id=%d" % id
        cursor.execute(sql)
        # fetchone return type is tuple
        result = cursor.fetchone()
        path = result[0]
        print("search_img success")
        return path
    except:
        # db.rollback()
        print("search_img failed")
        return False

def update_img(id, path):
    try:
        db = MysqlUtils.db
        cursor = db.cursor()
        sql = "update images set image_path='%s' where id=%d" % (path, id)
        cursor.execute(sql)
        print("update_img success")
        db.commit()
        return True
    except:
        db.rollback()
        print("update_img failed")
        return False

def delete_img(id):
    try:
        db = MysqlUtils.db
        cursor = db.cursor()
        sql = "select image_path from images where id=%d" % id
        cursor.execute(sql)
        # fetchone return type is tuple
        result = cursor.fetchone()
        path = result[0]
        if os.path.isfile(path):
            os.remove(path)
        sql = "delete from images where id=%d" % id
        cursor.execute(sql)
        print("delete_img success")
        db.commit()
        return True
    except:
        db.rollback()
        print("delete_img failed")
        return False