def getInput(): #function to check if the input is a number
    global value
    value = input()
    while not value.isnumeric():
        value = input("Please enter a number: ")
    return int(value)

print("********Enrolment System********")
i = 0
students = [] #List that will store all students
print("How many students do you want to enroll?")
numofstudents = getInput()
while i < numofstudents:
    dct = {}
    name = input("Please enter the student's name: ")
    dct["name"] = name

    ID = input("Please enter his/her ID: ")
    dct["ID"] = ID

    Mark = input("Please enter Mark: ")
    dct["Mark"] = Mark

    students.append(dct)
    i += 1

print(students)

