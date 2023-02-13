school_subject = ['Mathimatics', 'English', 'Italiano']


def tearcher_work(subject):
    path = school_subject[subject] + '.txt'
    try:
        with open(path, 'r', encoding='windows-1251') as file:
            lines = file.readlines()
    except:
        with open(path, 'w+', encoding='windows-1251') as file:
            lines = file.readlines()
    print("---List of students---")
    print("Write down the student's serial number: ")
    i = -1
    for i in range(len(lines)):
        lst = lines[i].split()
        print(f"{i + 1}. {lst[0]}")
    print(f"{i + 2}. The student is missing. Add Please. ")
    count = input("Your choice: ")
    while not (count.isdigit()) or int(count) > i + 2:
        count = input("Repeat the input: ")
    if int(count) == i + 2 or (int(count) - 2 == -1 and i == -1):
        student_add(subject)
    else:
        mark_add(subject, int(count))


def student_add(subject):
    print("---New student---")
    student = input("Add Last name of student: ")
    mark = input("Choose a mark: ")
    path = school_subject[subject] + '.txt'
    with open(path, 'a', encoding="windows-1251") as file:
        file.write(f"{student} {mark}\n")
    return


def mark_add(subject, student):
    path = school_subject[subject] + '.txt'
    with open(path, 'r+', encoding='windows-1251') as file:
        lines = file.readlines()
    i = 1
    new_lines = str()
    for line in lines:
        if i == student:
            lst = line.split()
            mark = input(f"The mark is: {lst[0]} ")
            lst.append(mark)
            str_lst = " ".join(lst)
            print(str_lst)
            line = str_lst + '\n'
        new_lines = new_lines + line
        i += 1
    with open(path, 'w') as file:
        file.write(new_lines)


def student_choose_subject():
    for i in range(len(school_subject)):
        print(f"{i + 1}. {school_subject[i]}")
    return int(input("Which subject? "))


def student_all_subject(student_name):
    lst_mark = str()
    for i in range(len(school_subject)):
        path = school_subject[i] + ".txt"
        try:
            with open(path, 'r') as file:
                lines = file.readlines()
            for line in lines:
                temp = line.split()
                if temp[0] == student_name:
                    lst_mark = lst_mark + school_subject[i] + ' - - ' + line
        except:
            lst_mark = lst_mark + school_subject[i] + '- - ' + student_name + " there is no marks"
    return lst_mark


def student_one_subject(student_name, subject):
    path = school_subject[subject - 1] + '.txt'
    try:
        with open(path, 'r') as file:
            lines = file.readlines()
    except:
        lines = ""
    if lines == "":
        print(f"There is no marks on'{school_subject[subject]}' ")
    else:
        lst_mark = str()
        for line in lines:
            temp = line.split()
            if temp[0] == student_name:
                for i in range(1, len(temp)):
                    lst_mark = lst_mark + temp[i] + ' '

    return lst_mark