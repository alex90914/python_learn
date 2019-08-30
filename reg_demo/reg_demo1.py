import re


class Emp(object):
    country = 'Chinese'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_age(self):
        return self.age

    @staticmethod
    def get_country():
        return Emp.country

    @classmethod
    def class_method(cls):
        return cls.country

    @property
    def get_age_pro(self):
        return self.get_age()


def main():
    pattern = r'^\d{1,6}@(126|128)\.com$'
    match_str = '100861@126.com'
    ret = re.match(pattern, match_str)
    if ret:
        print("匹配成功:%s" % ret.group())
    else:
        print("匹配失败:%s" % match_str)


if __name__ == '__main__':
    emp = Emp('张三', 25)
    print(emp.__dict__)
    print(Emp.__dict__)
    print(emp.get_age())
    print(Emp.get_country())
    print(Emp.class_method())
    print(emp.get_age_pro)
    main()
