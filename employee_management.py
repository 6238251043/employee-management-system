employees = {}

while True:
    print("\n1.Add Employee")
    print("2.View Employees")
    print("3.Search Employee")
    print("4.Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        emp_id = input("Employee ID: ")
        name = input("Employee Name: ")
        employees[emp_id] = name
        print("Employee Added")

    elif choice == "2":
        print(employees)

    elif choice == "3":
        emp_id = input("Enter ID: ")
        if emp_id in employees:
            print("Employee:", employees[emp_id])
        else:
            print("Not Found")

    elif choice == "4":
        break
