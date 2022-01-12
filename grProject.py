import csv
from csv import writer
import pandas as pd


def login():
    inp = input('if you are user press U or u: / if you are admin press A or a: ')
    if inp == 'A' or inp == 'a':
        passWord = str(input('please enter your password: '))
        # print(type(passWord))
        if passWord == 'RMIT':
            print('login successful')
            adminWindow()
        else:
            print('input is invalid. Please try again. ')
            login()
    elif inp == 'U' or inp == 'u':
        user = input("Please type 'User' to ensure that you are human : ")
        if user == 'User':
            print('login successful')
            userinfo()
            userChoice()
        else:
            print('input is invalid. Please try again. ')
            login()
    else:
        print('Input is invalid. Please try again. ')
        login()


def adminWindow():
    print('Press 1 to see list of customer: ')
    print('Press 2 to add add new items: ')
    print('Press 3 to see the list of items')
    print('Press 4 to logout')
    n = int(input())
    if n == 1:
        listOfCustomer()
        print('=========================')
        print('Go back to the main page')
        adminWindow()
    elif n == 2:
        addNewItem()
        print('=========================')
        print('Go back to the main page')
        adminWindow()
    elif n == 3:
        sortList()
        print('=========================')
        print('Go back to the main page')
        adminWindow()
    elif n == 4:
        logout()


def addInfoCus():
    print("Press 0 to see the list of customer's info. ")
    print("Otherwise enter the no.of.customer's info need to be added")
    n = int(input())
    if n == 0:
        listOfCustomer()
        for f in listOfCus:
            print(f)
    elif n != 0:
        for i in range(n):
            add_Name = input("Enter Name : ")
            add_MailAddress = input("Enter mail address : ")
            add_shippingAddress = input("Enter shipping adress : ")
            d = [{"Name": add_Name, "Mail address": add_MailAddress, "shipping address": add_shippingAddress}]
            listOfCus.extend(d)
        listOfCustomer()
        for f in listOfCus:
            print(f)


listOfCus = []


def listOfCustomer():
    df = pd.read_csv('u1.csv')
    print(df)

#print(listOfCustomer())
def menu():
    print('Here is the list of available items: ')
    data1 = pd.read_csv('listItem.csv', names=["ID", "Name", "quanlity", "colour", "size", "prize"])


def bestSeller():
    print('================================')
    print('Here is the list of best seller: ')
    bestSell = pd.read_csv('listItem.csv')
    print(bestSell.loc[1:19:5])
    print('================================')
    print()


listItem = []


def listOfItem():
    # print('Here is list of available item')
    filename = "listItem.csv"
    # opening the file using "with"u
    # statement
    with open(filename, 'r') as data:
        for line in csv.DictReader(data):
            listItem.append(line)



def sortList():
    listOfItem()
    print('Here is list of available items: ')
    print("Id\t\tName\t\tAvailable\t\tPrice")
    for d in listItem:
        print(f'{d["ID"]}\t\t{d["Name"]}\t\t{d["quanlity"]}\t\t\t\t{d["price"]}')


def addNewItem():
    num = int(input('please enter amount of new items: '))
    for i in range(num):
        list_data = ['ID', 'Name', 'quanlity', 'colour', 'size', 'prize']
        list_data[0] = input('New ID: ')
        list_data[1] = input('new name: ')
        list_data[2] = input('quanlity: ')
        list_data[3] = input('colour: ')
        list_data[4] = input('size: ')
        list_data[5] = input('prize: ')
        with open('listItem.csv', 'a', newline='') as f_object:
            # Pass the CSV  file object to the writer() function
            writer_object = writer(f_object)
            # Result - a writer object
            # Pass the data in the list as an argument into the writerow() function
            writer_object.writerow(list_data)
            # Close the file object
            f_object.close()

def userWindow1():
    print('press 1 for Menu: ')
    print('press 2 for logout: ')


def userWindow2():
    print('press 1 for PlaceOrder: ')
    print('press 2 for logout: ')




def userinfo():
    list_data = ['name', 'mail', 'address']
    list_data[0] = input("user's name: ")
    list_data[1] = input("mail: ")
    list_data[2] = input("address: ")
    with open('u1.csv', 'a', newline='') as f_object:
        # Pass the CSV  file object to the writer() function
        writer_object = writer(f_object)
        # Result - a writer object
        # Pass the data in the list as an argument into the writerow() function
        writer_object.writerow(list_data)
        # Close the file object
        f_object.close()


User = []


def userChoice():
    userWindow1()
    choice1 = input()
    if int(choice1) == 1:
        # menu()
        sortList()
        bestSeller()
        # listOfItem()
        userWindow2()
        choice2 = input()
        if int(choice2) == 1:
            PlaceOrder()
        elif int(choice2) == 2:
            logout()
        else:
            print('Input is wrong. Try again')
            userChoice()
    elif int(choice1) == 2:
        logout()
    else:
        userChoice()


# deleted old PlaceOrder function

def PlaceOrder():
    object = input("Enter item's name or item's id that you want to search: ")
    for d in listItem:
        if d["Name"] == object or d["ID"] == object:
            print('input correct: ')
            print(f'{d["ID"]} \t {d["Name"]} \t {d["quanlity"]} \t {d["price"]}')
            print('if you will get discount 10% for total bill if you buy at least 10 items')
            num = int(input('how many items do you want to buy? '))
            if int(d["quanlity"]) >= num >= 10:
                print('you got 10% discount.')
                print('the total prize is:', num * int(d["price"]) - num * int(d["price"]) * 0.1, 'VND')  # discount 10%
            elif num < 10:
                print(num * int(d["price"]) * 0.9, 'VND')
            if num > int(d["quanlity"]):
                b = int(input("Sorry we don't have enough items for you. Please press 1 if you want to try again. "
                              "Press 2 if you want to logout. "))
                if b == 1:
                    userChoice()
                elif b == 2:
                    logout()
            confirm()
            break
    if d["Name"] != object and d["ID"] != object:
        print('invalid')
        print('please input again: ')
        PlaceOrder()


def confirm():
    inp1 = input('Do you want to place an order Y/N: ')
    if inp1 == 'y' or inp1 == 'Y':
        print()
        print('===========================================')
        print('congratulation, your order is successful.')
        print("press 1 for go back to the main page")
        print('press 2 for exit')
        c = int(input())
        if c == 1:
            login()
        elif c == 2:
            logout()
    elif inp1 == 'n' or inp1 == 'N':
        print('cancel')
        print('return to the main page')
        login()


def logout():
    # to stop running
    print()


login()
