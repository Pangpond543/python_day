with open("employees.txt", "r") as file:
    count = file.read()
    while count:
        name = count.readline()
        print("Name: " + name)
        id = count.readline()
        print("ID number: " + id)
        department = count.readline()
        print("Department: " + department)
