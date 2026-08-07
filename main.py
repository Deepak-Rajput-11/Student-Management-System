from student import Student

students = []

running = True

while running:
    print("============================")
    print(" Student Management System  ")
    print("============================")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice : ")

    if choice == "1":
        print("Add Student Selector")
        student_id = input("Enter Student ID: ")
        name = input("Enter name: ")
        phone_number = input("Enter Phone Number: ")
        email = input("Enter Email: ")
        course = input("Enter Course Name: ")
        age = int(input("Enter age: "))
        guardian_name = input("Enter Guardian Name: ")
        address = input("Enter Address: ")

        student = Student(
            student_id,
            name,
            phone_number,
            email,
            course,
            age,
            guardian_name,
            address,
        )

        students.append(student)
        print("Student added successfully!")

    elif choice == "2":
        print("View Student Selector")
        print()

        if students == []:
            print("No Students Found")
        else:
            for student in students:
                print(f"ID: {student.student_id}")
                print(f"Name: {student.name}")
                print(f"Course: {student.course}")
                print(f"Age: {student.age}")
                print()

    elif choice == "3":
        search_id = input("Enter Student ID: ")
        found = False

        for student in students:
            if student.student_id == search_id:
                found = True
                print(f"ID: {student.student_id}")
                print(f"Name: {student.name}")
                print(f"Course: {student.course}")
                print(f"Age: {student.age}")
                print()
                break

        if found == False:
            print("Student not found.")

    elif choice == "4":
        delete_id = input("Enter Student ID: ")
        found = False

        for i in range(len(students)):
            if students[i].student_id == delete_id:
                found = True
                students.pop(i)
                print("Student deleted successfully!")
                break

        if found == False:
            print("Student not found.")

    elif choice == "5":
        print("Thanks for using Student Management System")
        running = False

    else:
        print("Invalid Choice")
