from student import Student
print("============================")
print(" Student Management System  ")
print("============================")

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

print(student1.name)
print(student2.name)