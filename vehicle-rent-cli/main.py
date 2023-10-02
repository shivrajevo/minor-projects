import os
import model
from datetime import date

INDEX_ID = 0

# a list for runtime memory
runtimememory = []


# function for option list
def options(listno, title=""):
    """for print a specfic list for cli interfice

    Args:
        listno (int): number of list
        title (str, optional): title for list. Defaults to "".
    """
    os.system("cls")  # it clear the screen
    print(title)

    match (listno):
        case 1:
            print(
                " 1 Create new \n",
                "2 View\n",
                "3 Delete\n",
                "4 Update \n",
                "0 EXIT",
            )
        case 2:
            # for creation
            print(
                " 1 for Car \n",
                "2 for Bike\n",
                "3 for Truck\n",
                "4 for Plane\n",
                "0 for Back",
            )
        case 3:
            # for view section
            print(
                " 1 view all \n",
                "2 car only\n",
                "3 Bike only\n",
                "4 Trck only\n",
                "5 plane only\n",
                "0 go back\n",
            )


def datestemp():
    """manually or auto date stemping

    Returns:
        str: date in string format
    """
    print(
        "SET DATE FIRST \n For manual enter date press '1'\n For autostemp press enter "
    )
    mode = input(" ---> ")
    if mode == "1":
        print("format year 2001 : month 02 : day 06 ")
        year = int(input("enter the year :"))
        month = int(input("enter the month :"))
        day = int(input("enter the day :"))

        os.system("cls")
        return str(date(year, month, day))

    else:
        os.system("cls")
        return str(date.today())


def rentfinder(olddate, rent, taxper):
    """find the rent sub oldate from newdate
    after that multiply the days winth rent and
    find tax from amount.

    Args:
        olddate (strng): date in string format
        rent (int): rent in integer
        taxper (int): tax persentage

    Returns:
        array : INDEX 0:total rent 1: tax on total rent 2: add tax with total amount
    """
    dateold = olddate
    datenew = date.today()
    year = ""
    month = ""
    day = ""
    seprate = 0
    # date extractor loop
    for i in dateold:
        if i == "-":
            seprate += 1
            continue

        if seprate == 0:
            year += i
        if seprate == 1:
            month += i
        if seprate == 2:
            day += i
    # date generator
    dateold = date(int(year), int(month), int(day))
    difference = datenew - dateold

    # calculated total rent
    totalrent = int(difference.days) * rent

    # rent calculator
    if totalrent < rent:
        totalrent = rent
    tax = taxper / 100
    tax = totalrent * tax
    totalamount = totalrent + tax

    return [totalrent, tax, totalamount]


def views(viewno):
    """for view the data in runtime memory
    actual datafetcher function

    Args:
        viewno (int): for selection of a specfic view
    """
    # to select global runtime memory
    global runtimememory

    # for print index of each object
    objindex = 0
    if len(runtimememory) == 0:
        print("NO DATA MEMORY EMPTY")
    else:
        # for print all view
        if viewno == 0:
            for obj in runtimememory:
                print(
                    objindex,
                    rentfinder(obj.date, obj.rentperday, obj.tax),
                    obj.getdatainlist(),
                )
                objindex += 1
        # for print car objcts only
        elif viewno == 1:
            for obj in runtimememory:
                objarray = obj.getdatainlist()
                if objarray[0] == "Car":
                    print(
                        objindex,
                        rentfinder(obj.date, obj.rentperday, obj.tax),
                        objarray,
                    )
                objindex += 1
        # for print Bike only
        elif viewno == 2:
            for obj in runtimememory:
                objarray = obj.getdatainlist()
                if objarray[0] == "Bike":
                    print(
                        objindex,
                        rentfinder(obj.date, obj.rentperday, obj.tax),
                        objarray,
                    )
                objindex += 1
        # for print Truck only
        elif viewno == 3:
            for obj in runtimememory:
                objarray = obj.getdatainlist()
                if objarray[0] == "Truck":
                    print(
                        objindex,
                        rentfinder(obj.date, obj.rentperday, obj.tax),
                        objarray,
                    )
                objindex += 1
        # for print plane only
        elif viewno == 4:
            for obj in runtimememory:
                objarray = obj.getdatainlist()
                if objarray[0] == "Plane":
                    print(
                        objindex,
                        rentfinder(obj.date, obj.rentperday, obj.tax),
                        objarray,
                    )
                objindex += 1
        else:
            print("wrong input dev")
    input("press Enter")


def viewselector():
    """a function that select the view according user input"""
    match (input(":: enter option number -> ")):
        case "1":
            # for all
            views(0)

        case "2":
            # for car
            views(1)

        case "3":
            # for bike
            views(2)

        case "4":
            # for truck
            views(3)

        case "5":
            # for plane
            views(4)


def deletedata():
    """function for delete the object for runtime list memory"""
    global runtimememory

    options(3, "SELECT VIEW MODE")

    viewselector()

    indexno = int(input("enter index no for delete # "))
    print(runtimememory[indexno].getdatainlist())
    del runtimememory[indexno]
    input("is delete press enter for exit")


def updatedata():
    """for update the selected object data using object method"""
    global runtimememory
    options(3, "SELECT VIEW TO SEE DATA")
    viewselector()
    indexno = int(input("enter index no for update # "))
    print(runtimememory[indexno].getdatainlist())
    runtimememory[indexno].updateit(datestemp())
    print(runtimememory[indexno].getdatainlist())
    input("is updated press enter for exit")


# count
count = 1

# status for menu
status = " "
# main menu loop  CLI HENDLER LOGIC
while True:
    options(1, "YOU ARE IN MAIN MENU")

    # option match case
    match (input(":: enter option number -> ")):
        case "1":
            # option 1 inner loop
            while True:
                options(2, "SELECT VEHICLE FOR RENT")
                match (input(":: enter option number -> ")):
                    case "1":
                        os.system("cls")
                        obj = model.caronrent(datestemp())
                        runtimememory.append(obj)
                        input("new record of car created ! PRESS ENTER")

                    case "2":
                        os.system("cls")
                        obj = model.bikeonrent(datestemp())
                        runtimememory.append(obj)
                        input("new record of bike created ! PRESS ENTER")
                    case "3":
                        os.system("cls")
                        obj = model.truckonrent(datestemp())
                        input("new record of truck created ! PRESS ENTER")
                        runtimememory.append(obj)
                    case "4":
                        os.system("cls")
                        obj = model.planeonrent(datestemp())
                        runtimememory.append(obj)
                        input("new record of plain created ! PRESS ENTER")
                    case "0":
                        print("abort")
                        break
                    case _:
                        print("not found")

        case "2":
            # view mode selector case
            options(3, "VIEW MODE SELECT STYLE")
            viewselector()

        case "3":
            deletedata()
        case "4":
            updatedata()
        case "0":
            os.system("cls")
            print("GOOD BYE !")
            break
        case _:
            if count == 3:
                exit()

# print(rentfinder("2021-6-12", 100, 10))
