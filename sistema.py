import os
import sys
import time
import getpass
import bcrypt
from tabulate import tabulate

salt = bcrypt.gensalt()

def login():

    print("\nPlease enter your username and password")
    username = input("Username: ")
    password = getpass.getpass("Password: ")

    hashed = b'$2b$12$x.7LkLdMP6BklkPMFkLslO3uWIMkbDXwSfRzBbCtME9iu/2wLHACa' # admin bcrypt hash

    if (bcrypt.checkpw(password.encode('utf-8'), hashed) and username == "admin"):
        print("\n\033[32m *** Login Success ***\033[m\n")
        #os.system("cls" if os.name == "nt" else "clear") # clear screen in all OSes
        main_menu()
    else:
        print("\n\033[31mThe username or password is incorrect\033[m\n")
        login()


def main_menu():
    print("Select one of the options below:")
    print("[1] Show Interfaces \n[2] Quit")
    interface = input(">")
    if interface == "2":
        print("saindo do programa")

    elif interface != "1":
        print("Command not accepted!\n")
        main_menu()
    else:    
        ifconfig = os.popen("ifconfig | grep 'ether\|broadcast\|eth\|inet \|br'").read()

        lines = ifconfig.split("\n")
        three_line_arr = []
        datas = []

        for i in range(0, len(lines)-4, 3):
            three_line_arr.append(lines[i:i+3]) # divide paragraphs of 3 lines (removing the last one because it's local)

        for paragraph in three_line_arr:
            up_or_down = "UP" if paragraph[0].find("UP") != -1 else "DOWN" 
            mtu = paragraph[0].split()[3] # get the 4th word of the first line
            inet = paragraph[1].split()[1] # get the 2nd word of the second line
            eth = paragraph[0].split()[0][:-1] #get the first word and remove last character of the first line
            mac = paragraph[2].split()[1] # get the 2nd word of the third line

        print("\033[36m==============================================\033[m")                     
        print("\033[36m*** Welcome to config linux network system ***\033[m")
        print("\033[36m==============================================\033[m")

    data = {
        'Intf': eth,
        'IP Address': inet,
        'MAC': mac,
        'MTU': mtu,
        'State':up_or_down
    }
    datas.append(data)    
    for data in datas:
        print(tabulate(datas, headers="keys", tablefmt="fancy_grid", showindex="always"))

login()