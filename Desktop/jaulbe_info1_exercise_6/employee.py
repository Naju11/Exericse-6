from vehicle import *
from customer import *


class Employee(object):
    ######## CODE MISSING HERE
    emp_id = 0

    def __init__(self, name):
        self.__id = Employee.emp_id + 1
        self.__name = name

    ######## CODE MISSING HERE

    def __str__(self):
        return "{0:s} is of type {1:s}".format(self.get_name(), self.get_title())

    ######## CODE MISSING HERE

    def get_name(self):
        return self.__name

    ######## CODE MISSING HERE

    def get_title(self):
        return "Subordinate"
        ######## CODE MISSING HERE


class Manager(Employee):
    def get_title(self):
        return "Manager"

    ######## CODE MISSING HERE

    def get_sales_report(self, salesman):
        if salesman not in Salesman.sales:
            raise KeyError("{0:s} does not have any Sales yet".format(salesman.get_name()))
        print("{0:s}'s current cumulative sales:".format(salesman.get_name()))
        print(Salesman.sales[salesman])
        ######## CODE MISSING HERE


class Salesman(Employee):
    ######## CODE MISSING HERE
    sales = {}

    def sale(self, vehicle, sales_price, customer):
        if customer.get_score():
            Salesman.sales[self] = Salesman.sales.get(self, 0) + sales_price
        else:
            print("The customer does not have enough credit score.")
            ######## CODE MISSING HERE


### test cases ###

## initialising employee instances

Eric = Manager("Eric")
Kyle = Employee("Kyle")
Stan = Salesman("Stan")
Kenny = Salesman("Kenny")
Craig = Salesman("Craig")

## printing employee instances

print(Eric)  # expected output: Employee: Eric is of type Manager
print(Kyle)  # expected output: Employee: Kyle is of type Subordinate
print(Stan)  # expected output: Employee: Stan is of type Subordinate
print(Kenny)  # expected output: Employee: Kenny is of type Subordinate
print(Craig)  # expected output: Employee: Craig is of type Subordinate

## registering sales

Kenny.sale(Veh2, 6000, Heidi)

Stan.sale(Veh1, 9000, Wendy)

## printing an individual sales report:

Eric.get_sales_report(Kenny)
# expected output:
# Kenny's current cumulative sales:
# 6000
