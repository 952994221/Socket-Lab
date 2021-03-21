# 数据库学生信息实体

class Student():
    def __init__(self, id, name, sex, age):
        self.id = id
        self.name = name
        self.sex = sex
        self.age = age

    def set_id(self, id):
        self.id = id

    def set_name(self, name):
        self.name = name

    def set_sex(self, sex):
        self.sex = sex

    def set_age(self, age):
        self.age = age

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_sex(self):
        return self.sex

    def get_age(self):
        return self.age
        
    def to_string(self):
        result = "%d %s %d %d" % (self.id, self.name, self.sex, self.age)
        return result
