# 1.Explore = will show the whole directory
# 2.Search = Will search using ID number or name
# 3.Add = Add data
# 4.Filter = Will filter using different criteria
# 5.Sorting = Sorting (ascending or descending)
# 6.Remove = Remove data
# 7.Edit = Edit data
# 8.Exit = Exit the program

students = {}
z = 0

def explore(call):
    if not call:
        print("No data available")
    else:
        for x, student in call.items():
            print(x)
            for data in student:
                print( data+ ' : ', student[data])

def search():
    name_id = input("Enter a name or ID: ")
    for x, student in students.items():
        if student['name'] != name_id:
            print("Student not found")
        elif student['name'] == name_id:
            print(x)
            for data in student:
                print(data + ' : ', student[data])

def add():
    x = input("Enter the name of the student: ")
    y = int(input("Enter the Roll of the student: "))
    global z
    z += 1
    students[f"student{z}"] = {"name" : x,
                               "Roll" : y}

def remove():
    name_id = input("Enter a name or ID: ")
    y = None
    for x, student in students.items():
        if student['name'] == name_id:
            y = x
    if y: students.pop(y)

def edit():
    name_id = input("Enter a name or ID: ")
    new_roll = int(input("Enter the new roll: "))
    for x, student in students.items():
        if student['name'] == name_id:
           student['Roll'] = new_roll

print('''
Welcome to the student directory of Sunnyside High-school
        
Enter 1 to see the database
Enter 2 to search
Enter 3 to add new data
Enter 4 to edit data
Enter 5 to remove
Enter 6 to filter
Enter 7 to sort
Enter 8 to exit
''')

while True:
    a = int(input("Enter your choice: "))
    if a == 1:
        explore(students)
    elif a == 2:
        search()
    elif a == 3:
        add()
    elif a == 4:
        edit()
    elif a == 5:
        remove()
    elif a == 8:
        print("Thank you")
        break
    else:
        print("Invalid Input")