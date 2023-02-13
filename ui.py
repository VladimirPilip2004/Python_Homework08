from database import (school_subject,
                      tearcher_work,
                      student_one_subject,
                      student_all_subject,
                      student_choose_subject)
import controller


def tearcher():
    print("----------------")    
    print("|   THEACHER   |")
    print("----------------")    
    print('What kind of subject do you put a marks?')
    for i in range(len(school_subject)):
        print(f"{i + 1}. {school_subject[i]}")
    disc = int(input("Your choice is: ")) - 1
    tearcher_work(disc)
    print('------------')
    print('1. Choose another subject')
    print('2. Return to Main menu')
    menu = 0
    while menu != 1 or menu != 2:
        menu = int(input("Your choice is: "))
        if menu == 1:
            tearcher()
            break
        elif menu == 2:
            controller.initial()
            break
        else:
            print("Please repeat enter")


def student():
    print("----------------")    
    print("|    STUDENT   |")
    print("----------------") 
    stud_name = input("Please enter your Last name: ")
    print("1. View marks by subject")
    print("2. View all marks")
    student_choose = int(input('Your choice is: '))
    if student_choose == 1:
        discip = student_choose_subject()
        list_mark = student_one_subject(stud_name, discip)
    elif student_choose == 2:
        list_mark = student_all_subject(stud_name)
    else:
        controller.initial()
    if len(list_mark) > 0: print(list_mark)
