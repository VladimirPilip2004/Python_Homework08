from ui import (tearcher, student)

def initial():
    choose = 0
    while choose != 3:
        print("-----------------")
        print("|   MAIN MENU   |")
        print("-----------------")
        print("1. Teacher")
        print("2. Student")
        print("3. Exit")
        choose = int(input("Choose your status! "))
        if choose == 1:
            tearcher()
        elif choose == 2:
            student()
        else:
            break