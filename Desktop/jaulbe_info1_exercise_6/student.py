from module import *


class Student(object):

    def __init__(self, name):
        self.name = name
        self.modules =  []
        self.grades = {}
        ######## CODE MISSING HERE

    def add_module(self,title):
        self.modules.append(title)
        self.grades[title] = self.get_grades()
        ######## CODE MISSING HERE

    def get_list_modules(self):
        print("Modules of %s:" %self.name)
        for module in self.modules:
            print ("\t{0:s}".format(module.get_title()))
        ######## CODE MISSING HERE

    def get_grades(self):
        print("Grades of student %s:" %self.name)
        for x in self.grades:
            print("\t%s: %s" %(x.get_title(), x.get_grade()))
        ######## CODE MISSING HERE


### test cases ###

me = Student("FirstName LastName")
me.add_module(info1)
me.get_list_modules()
# expected output:
# Modules of Student FirstName LastName:
#	Info 1

me.get_grades()
# expected output:
# Grades of Student FirstName LastName:
#	Info 1: 6
