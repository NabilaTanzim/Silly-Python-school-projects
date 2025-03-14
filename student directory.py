# 1.Explore = will show the whole directory
# 2.Search = Will search using ID number or name
# 3.Add = Add data
# 3.Filter = Will filter using different criteria
# 4.Sorting = Sorting (ascending or descending)
# 5.Remove = Remove data
# 6.Edit = Edit data
# 7.Exit = Exit the program

students = { "Student1" : {"name" : "Ilma",
                            'Roll' : 5} }

def explore(students):
    for student in students.items():
        print(student)
        for data in student:
            print( data+ ' : ', student[data])

explore(students)