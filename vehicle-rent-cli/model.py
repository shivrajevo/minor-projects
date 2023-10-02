from copy import copy
import datetime
import os


os.system("cls")


# base class for all types of vehicle
class base:
    vehicle = ""
    tax = int()

    def __init__(self, date):
        self.date = date
        print(f"------------------------------\n>> Enter the details of {self.vehicle}")
        self.vehiclename = input(f"enter the name of {self.vehicle} : ")
        self.rentperday = int(input(f"rent on {self.vehicle} per day $ : "))
        print(f"------------------------------\n>>Enter the details of person ")
        self.person = input(f"enter the name of person : ")
        self.address = input("enter the full adress of person : ")
        self.mobile = input("enter the mobile no : ")

    def getdatainlist(self):
        return [
            self.vehicle,
            self.vehiclename,
            self.rentperday,
            self.tax,
            self.date,
            self.person,
            self.address,
            self.mobile,
        ]

    def updateit(self, date):
        temp = ""
        print("Press ENTER ONLY TO IGNORE updation")
        if input("update date :"):
            self.date = date
        temp = input(f"enter new name of {self.vehicle} : ")
        if temp != "":
            self.vehiclename = temp
            temp = ""
        temp = input("update rent perday $ : ")
        if temp != "":
            self.rentperday = int(temp)
            temp = ""
        temp = input("enter new name :")
        if temp != "":
            self.person = temp
            temp = ""
        temp = input("Enter new address :")
        if temp != "":
            self.address = temp
            temp = ""
        temp = input("Update number :")
        if temp != "":
            self.mobile = int(temp)


# class for different type of vehicle


class caronrent(base):
    def __init__(self, date):
        self.vehicle = "Car"
        self.tax = 15
        super().__init__(date)


class bikeonrent(base):
    def __init__(self, date):
        self.vehicle = "Bike"
        self.tax = 12
        super().__init__(date)


class truckonrent(base):
    def __init__(self, date):
        self.vehicle = "Truck"
        self.tax = 25
        super().__init__(date)


class planeonrent(base):
    def __init__(self, date):
        self.vehicle = "Plane"
        self.tax = 30
        super().__init__(date)


if __name__ == "__main__":
    datestemp = datetime.datetime.now()
    datestemp2 = datetime.datetime.now()

    obj = bikeonrent("timestemp")
    # print(obj.vehicle)
    print(obj.vehicle)
    obj.getdatainlist()
