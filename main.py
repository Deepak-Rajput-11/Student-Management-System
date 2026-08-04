from student import Student
students = []


student1 = Student(
    "SMS100",
    "Deepak",
    "9878987898",
    "deepak@gmail.com",
    "BCA",
    21,
    "ABC",
    "Ambala"
)

student2 = Student(
    "SMS101",
    "Rahul",
    "987777898",
    "rahul@gmail.com",
    "BCA",
    21,
    "ABC",
    "Mohali"
)


running = True

while running:
 print("============================")
 print(" Student Management System  ")
 print("============================")
 print("1. Add Student")
 print("2. View Students")
 print("3. Exit")

 choice = input("Enter your choice : ")
 if choice == "1":
    print("Add Student Selector")
    student_id = input("Enter Student ID: ")
    name = input("Enter name: ")
    phone_number = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    course = input("Enter Course Name: ")
    age = int(input("Enter age: "))
    guardian_name = input("Enter Gaurdian Name: ")
    address = input("Enter Address: ")

    # Create Student object here
    student = Student(
    student_id,
    name,
    phone_number,
    email,
    course,
    age,
    guardian_name,
    address
    )
    students.append(student)
    print("Student added successfully!")

 elif choice == "2":
    print("View Student Selector")
 elif choice == "3":
    print("Thanks for using Student Management System")
    running = False
 else:
    print("Invalid Choice")