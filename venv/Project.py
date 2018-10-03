import re
import os
import random
#class that initializes all objects
class Employee():
    allemployees = []
    number_of_employees = 0
    def __init__(self, first, last, pay, idnr=None):
        self.allemployees.append(self)
        self.first = first
        self.last = last
        self.pay = pay
        if idnr == None:
            idrandom = 0
            while idrandom == 0:
                randidnr = random.randint(1000, 9999)
                for all in Employee.allemployees:
                    if randidnr == all.idnr:
                        break
                    else:
                        self.idnr = str(randidnr)
                        idrandom += 1
                        break
        else:
            self.idnr = idnr
        self.email = "{}.{}@Company.com".format(self.first, self.last)
        Employee.number_of_employees += 1
    def setfirst(self, first):
        self.first = first
    def setlast(self, last):
        self.last = last
    def setpay(self, pay):
        self.pay = pay
    def setidnr(self, idnr):
        self.idnr = idnr

#child class of Employee, initializes developer specific attributes but lets the parents class init initialize the general attributes
class Developer(Employee):
    alldevelopers = []
    def __init__(self, first, last, pay, plang, idnr=None):
        super().__init__(first, last, pay, idnr)
        Developer.alldevelopers.append(self)
        self.plang = plang
    def setplang(self, plang):
        self.plang = plang

#child class of Employee, initializes manager specific attributes but lets the parents class init initialize the general attributes
class Manager(Employee):
    allmanagers = []
    def __init__(self, first, last, pay, companycar, idnr=None):
        super().__init__(first, last, pay, idnr)
        self.companycar = companycar
    def setcompanycar(self, companycar):
        self.companycar = companycar

#function to write all instantiated objects to disk
def writetodisk():
    with open("employees.txt","w") as file:
        for all in Employee.allemployees:
            if all.first == None:
                continue
            elif re.search(".Employee.", str(all)) != None:
                file.write("Employee: {} {} {} {}\n".format(all.first, all.last, all.pay, all.idnr))
            elif re.search(".Developer.", str(all)) != None:
                file.write("Developer: {} {} {} {} {}\n".format(all.first, all.last, all.pay, all.plang, all.idnr))
            elif re.search(".Manager.", str(all)) != None:
                file.write("Manager: {} {} {} {} {}\n".format(all.first, all.last, all.pay, all.companycar, all.idnr))

#function to load from existing employee register
def loadingfromfile():
    with open("employees.txt", "r") as fh:
        for line in fh:
            line = line.split()
            if line[0] == "Employee:":
                Employee(line[1], line[2], line[3], line[4])
            if line[0] == "Developer:":
                Developer(line[1], line[2], line[3], line[4], line[5])
            if line[0] == "Manager:":
                Manager(line[1], line[2], line[3], line[4], line[5])

#checks if file exists, creates file if it doesnt exist, loads from file if it does exist
exists = os.path.isfile("employees.txt")
if exists == False:
    fh = open("employees.txt", "w")
    print("No employee file detected, creating one")
    fh.close()
elif exists == True:
    print("Employee register detected, loading data")
    loadingfromfile()

#start of interactive part
print("------------------------------------------")
print("Welcome to the Employee Management System")
print("------------------------------------------")
while True:
    #initial menu
    start = input("What would you like to do? \n"
                  "[A]dd employee \n"
                  "[D]elete employee \n"
                  "[C]hange employee info\n"
                  "[F]ind if employee is in system\n"
                  "[L]ist of all employees in system\n"
                  "\n"
                  "[Q]uit\n"
                  ">> ").lower()
    #start of add employee block
    if start == "a":
        while True:
            #start of general attributes input block
            positioninput = input("What position will the new employee hold?\n"
                                  "[D]eveloper\n"
                                  "[M]anager\n"
                                  "[O]ther\n"
                                  "\n"
                                  "[B]ack\n"
                                  ">> ").lower()
            if positioninput == "b":
                break
            elif positioninput == "d" or positioninput == "m" or positioninput == "o":
                sure = 0
                empadded = 0
                while sure == 0:
                    #first name input
                    firstinput = input("Firstname?\n>> ").lower()
                    if len(firstinput.split()) != 1:
                        print("Please enter only firstname")
                        continue
                    else:
                        break
                while True:
                    #last name input
                    lastinput = input("Lastname?\n>> ").lower()
                    if len(lastinput.split()) != 1:
                        print("Please enter only lastname")
                        continue
                    else:
                        break
                while True:
                    #pay input
                    payinput = input("Pay?\n>> ")
                    if len(payinput.split()) != 1:
                        print("Please enter a number, no spaces")
                        continue
                    else:
                        #makes sure input is a number
                        try:
                            if int(payinput) < 0:
                                print("Pay must be 0 or greater")
                            else:
                                break
                        except:
                            print("Please enter numbers only")
                if positioninput == "o":
                    while True:
                        #checks if user is okay with input information
                        correctinfo = input("Is this info correct:\nFirstname: {}\nLastname: {}\nPay:{}\n[Y]es [N]o\n>> ".format(firstinput, lastinput, payinput)).lower()
                        if correctinfo == "y":
                            Employee(firstinput, lastinput, payinput)
                            print("Employee has been added")
                            sure +=1
                            empadded +=1
                            break
                        elif correctinfo == "n":
                            print("Scrapping data and restarting the add employee process.")
                            break
                        else:
                            print("Please answer [Y]es or [N]o")
                            continue
                #start of developer attributes input block
                if positioninput == "d":
                    while True:
                        proglanginput = input("What programming language will the employee work with\n>> ").lower()
                        if len(proglanginput.split()) != 1:
                            print("Please enter a programming language, no spaces")
                            continue
                        else:
                            break
                    while True:
                        # checks if user is okay with input information
                        correctinfo = input("Is this info correct:\nFirstname: {}\nLastname: {}\nPay: {}\nProgramming language: {}\n[Y]es [N]o\n>> ".format(firstinput,lastinput,payinput,proglanginput)).lower()
                        if correctinfo == "y":
                            Developer(firstinput, lastinput, payinput, proglanginput)
                            print("Employee has been added")
                            sure += 1
                            empadded += 1
                            break
                        elif correctinfo == "n":
                            print("Scrapping data and restarting the add employee process.")
                            break
                        else:
                            print("Please answer [Y]es or [N]o")
                            continue
                #start of manager attributes input block
                if positioninput == "m":
                    while True:
                        companycarinput = input("What brand of company car will the employee get\n>> ").lower()
                        if len(companycarinput.split()) != 1:
                            print("Please enter the brand of the car, no spaces")
                            continue
                        else:
                            break
                    while True:
                        # checks if user is okay with input information
                        correctinfo = input("Is this info correct:\nFirstname: {}\nLastname: {}\nPay: {}\nCompany car brand: {}\n[Y]es [N]o\n>> ".format(firstinput, lastinput, payinput, companycarinput)).lower()
                        if correctinfo == "y":
                            Manager(firstinput, lastinput, payinput, companycarinput)
                            print("Employee has been added")
                            sure += 1
                            empadded += 1
                            break
                        elif correctinfo == "n":
                            print("Scrapping data and restarting the add employee process.")
                            break
                        else:
                            print("Please answer [Y]es or [N]o")
                            continue
            else:
                print("{} is not a valid option, please enter a valid option".format(positioninput))
                continue
            if empadded != 0:
                #if employee was added, asks if user wants to add another employee
                addmoreinput = input("Would you like to add another employee? [Y]es [N]o\n>> ").lower()
                if addmoreinput == "y":
                    continue
                elif addmoreinput == "n":
                    break
        #writes to disk
        writetodisk()
    #start of change attribute block
    elif start == "c":
        while True:
            nothingfound = 0
            changeinput = input("Enter the ID number of the person whose info you wish to change, or [B]ack\n>> ")
            if changeinput == "b":
                break
            try:
                if int(changeinput) < 0:
                    print("Please enter a positive number")
                    continue
            except:
                print("Only numbers, please")
                continue
            else:
                for all in Employee.allemployees:
                    if all.idnr == changeinput:
                        nothingfound +=1
                        # start of non specialized employee attribute changes
                        if re.search(".Employee.", str(all)) != None:
                            stop = 0
                            print("Info for employee with idnr {}:\n\nFirstname: {}, Lastname: {}, Pay: {}\n".format(all.idnr, all.first, all.last,all.pay))
                            while stop == 0:
                                whatchange = input("What info would you like to change?\n"
                                                    "[F]irst name\n"
                                                    "[L]ast name\n"
                                                    "[P]ay\n"
                                                    "[N]othing\n"
                                                    ">> ").lower()
                                while True:
                                    #changes first name
                                    if whatchange == "f":
                                        fchange = input("Current first name is {}. What would you like to change it to\n>> ".format(all.first)).lower()
                                        if len(fchange.split()) == 1:
                                            print("{} has been changed to {}".format(all.first, fchange))
                                            all.setfirst(fchange)
                                            stop +=1
                                            break
                                        else:
                                            print("Only enter first name, please. Use hyphens for double names.")
                                    #changes last name
                                    elif whatchange == "l":
                                        fchange = input("Current last name is {}. What would you like to change it to\n>> ".format(all.last)).lower()
                                        if len(fchange.split()) == 1:
                                            print("{} has been changed to {}".format(all.last, fchange))
                                            all.setlast(fchange)
                                            stop += 1
                                            break
                                        else:
                                            print("Only enter last name, please. Use hyphens for double names.")
                                    #changes pay
                                    elif whatchange == "p":
                                        fchange = input("Current pay is {}. What would you like to change it to\n>> ".format(all.pay)).lower()
                                        #makes sure pay is a number and equal to or above 0
                                        try:
                                            if int(fchange) < 0:
                                                print("Pay has to be 0 or greater")
                                                continue
                                            if len(fchange.split()) == 1:
                                                print("{} has been changed to {}".format(all.pay, fchange))
                                                all.setpay(fchange)
                                                stop +=1
                                                break
                                            else:
                                                print("Only enter pay, please. No spaces")
                                        except:
                                            print("Enter numbers only please, no spaces")
                                    elif whatchange == "n":
                                        stop += 1
                                        break
                                    else:
                                        print("Enter a valid option, please")
                                        break

                        #start of developer attribute changes
                        elif re.search(".Developer.", str(all)) != None:
                            stop = 0
                            while stop == 0:
                                print("Info for employee with idnr {}:\n\nFirstname: {}, Lastname: {}, Pay: {}, Programming language: {}\n".format(all.idnr, all.first, all.last, all.pay, all.plang))
                                whatchange = input("What info would you like to change?\n"
                                                    "[F]irst name\n"
                                                    "[L]ast name\n"
                                                    "[P]ay\n"
                                                    "[Prog]ramming language\n"
                                                    "[N]othing\n"
                                                    ">> ").lower()
                                while True:
                                    if whatchange == "f":
                                        #changes first name of developer
                                        fchange = input("Current first name is {}. What would you like to change it to\n>> ".format(all.first)).lower()
                                        if len(fchange.split()) == 1:
                                            print("{} has been changed to {}".format(all.first, fchange))
                                            all.setfirst(fchange)
                                            stop +=1
                                            break
                                        else:
                                            print("Only enter first name, please. Use hyphens for double names.")
                                    elif whatchange == "l":
                                        #changes last name of developer
                                        fchange = input("Current last name is {}. What would you like to change it to\n>> ".format(all.last)).lower()
                                        if len(fchange.split()) == 1:
                                            print("{} has been changed to {}".format(all.last, fchange))
                                            all.setlast(fchange)
                                            stop +=1
                                            break
                                        else:
                                            print("Only enter last name, please. Use hyphens for double names.")
                                    elif whatchange == "p":
                                        #changes pay of developer
                                        fchange = input("Current pay is {}. What would you like to change it to\n>> ".format(all.pay)).lower()
                                        try:
                                            #makes sure pay is a number and greater than or equal to 0
                                            if int(fchange) < 0:
                                                print("Pay has to be 0 or greater")
                                                continue
                                            if len(fchange.split()) == 1:
                                                print("{} has been changed to {}".format(all.pay, fchange))
                                                all.setpay(fchange)
                                                stop +=1
                                                break
                                            else:
                                                print("Only enter pay, please. No spaces")
                                        except:
                                            print("Enter numbers only please, no spaces")
                                    elif whatchange == "prog":
                                        #changes programming language of programmer
                                        fchange = input("Current programming language is {}. What would you like to change it to\n>> ".format(all.plang)).lower()
                                        if len(fchange.split()) == 1:
                                            print("{} has been changed to {}".format(all.plang, fchange))
                                            all.setplang(fchange)
                                            stop +=1
                                            break
                                        else:
                                            print("Only programming language, please. Use hyphens instead of spaces if needed.")
                                    elif whatchange == "n":
                                        stop += 1
                                        break
                                    else:
                                        print("Enter a valid option, please")
                                        break

                        #start of manager attribute changes
                        elif re.search(".Manager.", str(all)) != None:
                            stop = 0
                            print("Info for employee with idnr {}:\n\nFirstname: {}, Lastname: {}, Pay: {}, Company car brand: {}\n".format(all.idnr, all.first, all.last, all.pay, all.companycar))
                            while stop == 0:
                                whatchange = input("What info would you like to change?\n"
                                                    "[F]irst name\n"
                                                    "[L]ast name\n"
                                                    "[P]ay\n"
                                                    "[C]ompany car brand\n"
                                                    "[N]othing\n"
                                                    ">> ").lower()
                                while True:
                                    if whatchange == "f":
                                        #changes first name of manager
                                        fchange = input("Current first name is {}. What would you like to change it to\n>> ".format(all.first)).lower()
                                        if len(fchange.split()) == 1:
                                            print("{} has been changed to {}".format(all.first, fchange))
                                            all.setfirst(fchange)
                                            stop +=1
                                            break
                                        else:
                                            print("Only enter first name, please. Use hyphens for double names.")
                                    elif whatchange == "l":
                                        # changes last name of manager
                                        fchange = input("Current last name is {}. What would you like to change it to\n>> ".format(all.last)).lower()
                                        if len(fchange.split()) == 1:
                                            print("{} has been changed to {}".format(all.last, fchange))
                                            all.setlast(fchange)
                                            stop +=1
                                            break
                                        else:
                                            print("Only enter last name, please. Use hyphens for double names.")
                                    elif whatchange == "p":
                                        # changes pay of manager
                                        fchange = input("Current pay is {}. What would you like to change it to\n>> ".format(all.pay)).lower()
                                        try:
                                            #makes sure pay is a number and equal to or greater than 0
                                            if int(fchange) < 0:
                                                print("Pay has to be 0 or greater")
                                                continue
                                            if len(fchange.split()) == 1:
                                                print("{} has been changed to {}".format(all.pay, fchange))
                                                all.setpay(fchange)
                                                stop +=1
                                                break
                                            else:
                                                print("Only enter pay, please. No spaces")
                                        except:
                                            print("Enter numbers only please, no spaces")
                                    elif whatchange == "c":
                                        #changes company car of manager
                                        fchange = input("Current company car brand is {}. What would you like to change it to\n>> ".format(all.companycar)).lower()
                                        if len(fchange.split()) == 1:
                                            print("{} has been changed to {}".format(all.companycar, fchange))
                                            all.setcompanycar(fchange)
                                            stop +=1
                                            break
                                        else:
                                            print("Only programming language, please. Use hyphens instead of spaces if needed.")
                                    elif whatchange == "n":
                                        stop += 1
                                        break
                                    else:
                                        print("Enter a valid option, please")
                                        break
                if nothingfound == 0:
                        print("No person with that idnr exists in the system")
        #writes to disk
        writetodisk()
    #start of find module
    elif start == "f":
        searchfor = input("What would you like to search by\n"
                          "[F]irst name\n"
                          "[L]ast name\n"
                          "[P]ay\n"
                          "[Prog]ramming language\n"
                          "[C]ompany car brand\n"
                          "\n"
                          "[N]othing\n"
                          ">> ").lower()
        if searchfor == "f":
            #searcing by first name
            searchname = input("What first name would you like to search for?").lower()
            errormessage = 0
            for all in Employee.allemployees:
                if all.first == searchname:
                    if re.search(".Employee.", str(all)) != None:
                        print(all.first, all.last, all.pay, all.idnr)
                        errormessage += 1
                    elif re.search(".Developer.", str(all)) != None:
                        print(all.first, all.last, all.pay, all.plang, all.idnr)
                        errormessage += 1
                    elif re.search(".Manager.", str(all)) != None:
                        print(all.first, all.last, all.pay, all.companycar, all.idnr)
                        errormessage += 1
            if errormessage == 0:
                print("Nothing found!")

        elif searchfor == "l":
            #searching by last name
            searchname = input("What last name would you like to search for?").lower()
            errormessage = 0
            for all in Employee.allemployees:
                if all.last == searchname:
                    if re.search(".Employee.", str(all)) != None:
                        print(all.first, all.last, all.pay, all.idnr)
                        errormessage +=1
                    elif re.search(".Developer.", str(all)) != None:
                        print(all.first, all.last, all.pay, all.plang, all.idnr)
                        errormessage += 1
                    elif re.search(".Manager.", str(all)) != None:
                        print(all.first, all.last, all.pay, all.companycar, all.idnr)
                        errormessage += 1
            if errormessage == 0:
                print("Nothing found!")

        elif searchfor == "p":
            #searching by pay
            searchname = input("What pay would you like to search for?")
            errormessage = 0
            for all in Employee.allemployees:
                if all.pay == searchname:
                    if re.search(".Employee.", str(all)) != None:
                        print(all.first, all.last, all.pay, all.idnr)
                        errormessage += 1
                    elif re.search(".Developer.", str(all)) != None:
                        print(all.first, all.last, all.pay, all.plang, all.idnr)
                        errormessage += 1
                    elif re.search(".Manager.", str(all)) != None:
                        print(all.first, all.last, all.pay, all.companycar, all.idnr)
                        errormessage += 1
            if errormessage == 0:
                print("Nothing found")

        elif searchfor == "prog":
            #searching by programming language
            searchname = input("What programming language would you like to search for?").lower()
            errormessage = 0
            for all in Employee.allemployees:
                if re.search(".Developer.", str(all)) == None:
                    continue
                else:
                    if all.plang == searchname:
                        print(all.first, all.last, all.pay, all.plang)
                        errormessage += 1
            if errormessage == 0:
                print("Nothing found!")


        elif searchfor == "c":
            #searching by company car
            searchname = input("What brand company car would you like to search for?").lower()
            errormessage = 0
            for all in Employee.allemployees:
                if re.search(".Manager.", str(all)) == None:
                    continue
                else:
                    if all.companycar == searchname:
                        print(all.first, all.last, all.pay, all.companycar)
                        errormessage +=1
            if errormessage == 0:
                print("Nothing found!")
        else:
            print("Please enter a valid option")


    #start of delete module
    elif start == "d":
        suredelete = 0
        while suredelete == 0:
            deleteinput = input("Enter idnr of the person you wish to delete from the system, or [B]ack").lower()
            if deleteinput == "b":
                break
            nofound = 0
            for all in Employee.allemployees:
                if all.idnr == deleteinput:
                    nofound +=1
                    while True:
                        #makes sure user wants to delete selected employee
                        deleteassurance = input("Are you sure you want to delete:\nFirstname: {}, Lastname: {}, idnr: {} [Y]es [N]o".format(all.first, all.last, all.idnr)).lower()
                        if deleteassurance == "y" :
                            print("Firstname: {}, Lastname: {}, idnr: {} has been deleted".format(all.first, all.last, all.idnr))
                            all.setfirst(None)
                            all.setlast(None)
                            all.setpay(None)
                            all.setidnr(None)
                            writetodisk()
                            Employee.allemployees = []
                            loadingfromfile()
                            break
                            suredelete +=1
                        elif deleteassurance == "n":
                            break
                        else:
                            print("Please answer [Y]es or [N]o")
                            continue
            if nofound == 0:
                print("No person with that idnr exists in the database")

    #start of list module
    elif start == "l":
        for all in Employee.allemployees:
            if re.search(".Employee.", str(all)) != None:
                print("Firstname: {}, Lastname: {}, idnr: {}".format(all.first, all.last, all.idnr))
            elif re.search(".Developer.", str(all)) != None:
                print("Firstname: {}, Lastname: {}, Programming language: {}, idnr: {}".format(all.first, all.last, all.plang, all.idnr))
            elif re.search(".Manager.", str(all)) != None:
                print("Firstname: {}, Lastname: {}, Company car brand: {}, idnr: {}".format(all.first, all.last, all.companycar, all.idnr))

        print("There are {} Employees in the system\n".format(Employee.number_of_employees))
    #start of quit module
    #writes all objects to disk and then quits
    elif start == "q":
        writetodisk()
        quit()

    else:
        print("{} is not a valid option, please enter a valid option".format(start))