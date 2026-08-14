# Student Management System

## Description

A Python-based Student Management System built from scratch as part of my Software Engineering learning journey. This project focuses on applying Object-Oriented Programming (OOP), Python fundamentals, and software development best practices.

## Feature Completed

### Day 1

- Student class using OOP
- Constructor (**init**)
- Object creation
- Importing classes
- Displaying student information

### Day 2

- Menu-driven program using while loop
- User input for adding students
- Dynamic Student object creation
- Stored Student objects in a list
- Exit option

### Day 3

- View Students feature
- Display student details using for loop
- Empty list validation
- Formatted output using f-strings

### Day 4

- Search Student feature
- Search student using Student ID
- Implemented search using for loop
- Used flag variable (`found`) to detect search result
- Optimized search using `break`
- Display student details if found
- Display "Student not found" message when ID does not exist

### Day 5

- Delete Student feature
- Delete student using Student ID
- Learned index-based loop using `for i in range(len(students))`
- Used `pop()` to remove a student from the list
- Display success message after deletion
- Display "Student not found" when ID does not exist

### Day 6

- Student search by ID
- Student deletion by ID
- Student information update by ID
- Updating object attributes dynamically
- Using `for` loop with `range()`
- Using `list.pop()` for deletion
- Using `found` flag for search/update/delete operations

### Day 7

- Added input validation for student age
- Learned and practically used `try` and `except`
- Handled `ValueError` for invalid age input
- Used `while True` to repeatedly request valid input
- Used `break` to exit the validation loop after valid input
- Applied age validation to both Add Student and Update Student
- Prevented the program from crashing when invalid age is entered

### Day 8

- Added duplicate Student ID validation
- Used a Boolean `duplicate` flag to track duplicate IDs
- Searched existing students using a `for` loop
- Prevented creation of students with duplicate IDs
- Added an error message when a Student ID already exists
- Improved data integrity of the Student Management System

### Day 9

- Added Student ID input validation
- Prevented empty Student IDs
- Used a `while` loop to repeatedly request valid input
- Used `if/else` to check whether the Student ID is empty
- Used `break` to exit the validation loop when valid input is provided
- Learned that `break` exits the current loop, not the entire program
- Improved the reliability of the Add Student feature

### Day 10

- Added phone number validation
- Used `.isdigit()` to check that the phone number contains only digits
- Used `len()` to check that the phone number contains exactly 10 digits
- Used the `and` operator to combine multiple validation conditions
- Added a loop to repeatedly ask for a phone number until valid input is entered
- Added basic email validation
- Used the `in` operator to check for `@` and `.` in an email address
- Used `while True` and `break` for email validation
- Tested both valid and invalid phone numbers
- Tested both valid and invalid email addresses
- Learned the importance of saving the file before running the latest changes

### Day 11

- Added phone number validation to Update Student
- Added email validation to Update Student
- Improved Search Student to display complete student details
- Improved View Students to display complete student details
- Added student numbering using `enumerate()`
- Improved formatting of student information for better readability
- Tested all changes successfully

## Technologies

- Python
- Object-Oriented-programming(OOP)

## Status

- Project in Progress
