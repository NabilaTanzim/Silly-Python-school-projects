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

def explore():
    if not students:
        print("No data available\n")
    else:
        for x, student in students.items():
            print(x)
            for data in student:
                print( data+ ' : ', student[data])
            print('\n')


def search():
    if not students:
        print("No data available\n")
    else:
        name_id = input("Enter a name or ID: ")
        data_found = False
        for x, student in students.items():
            if student['name'] == name_id:
                data_found = True
                print(x)
                for data in student:
                    print(data + ' : ', student[data])
                print('\n')

        if not data_found:
            print("Student not found.\n")


def add():
    x = input("Enter the name of the student: ")
    y = int(input("Enter the Roll of the student: "))
    global z
    z += 1
    students[f"student{z}"] = {"name" : x,
                               "Roll" : y}
    print("Information added successfully!!\n")


def remove():
    if not students:
        print("No data available\n")
    else:
        name_id = input("Enter a name or ID: ")
        to_remove = []
        data_found = False
        for x, student in students.items():
            if student['name'] == name_id:
                data_found = True
                b = input(f"Are you sure you want to delete the information of {name_id} (y/n): ")
                if b.lower() == 'n':
                    print('\n')
                    break
                elif b.lower() == 'y':
                    to_remove.append(name_id)

        for y in to_remove:
            del students[y]
            print("Information removed successfully!!")

        if not data_found:
            print("Student not found.\n")


def edit():
    if not students:
        print("No data available\n")
    else:
        name_id = input("Enter a name or ID: ")
        new_roll = int(input("Enter the new roll: "))
        data_found = False

        for x, student in students.items():
            if student['name'] == name_id:
                data_found = True
                b = input(f"Are you sure you want to update the information of {name_id} (y/n): ")
                if b.lower() == 'n':
                    print('\n')
                    break
                elif b.lower() == 'y':
                    student['Roll'] = new_roll
                    print("Data updated successfully")
        if not data_found:
            print("Student not found.\n")


def filtering():
    print("This feature is coming soon\n")


def sort():
    print("This feature is coming soon\n")


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

try:
    while True:
        a = int(input("Enter your choice: "))
        if a == 1:
            explore()
        elif a == 2:
            search()
        elif a == 3:
            add()
        elif a == 4:
            edit()
        elif a == 5:
            remove()
        elif a == 6:
            filtering()
        elif a == 7:
            sort()
        elif a == 8:
            print("Thank you")
            break
        else:
            print("Invalid Input\n")

except ValueError:
    print("Invalid Input")

# problems faced:
# 1. Does not take inputs after except condition
# 2. detects spaces as value error
# 3. does not take id yet
# 4. ID does not necessarily have to be in integer. str should be fine