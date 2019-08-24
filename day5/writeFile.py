employee_file = open("employee.txt","a")

employee_file.write("Human resources")

employee_file.close()

#2nd method

with open("employee.txt","r") as my_file:
    contents = my_file.readlines()
    for line in contents:
        print(line)