# Student Management System

## Description

A Python-based Student Management System built from scratch as part of my Software Engineering learning journey. This project focuses on applying Object-Oriented Programming (OOP), Python fundamentals, and software development best practices.

## Features Completed

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

### Day 12

- Improved duplicate Student ID validation
- Duplicate Student IDs now ask for a new ID instead of returning to the main menu
- Created a reusable `get_valid_phone()` function
- Used `get_valid_phone()` in Add Student and Update Student
- Created a reusable `get_valid_email()` function
- Used `get_valid_email()` in Add Student and Update Student
- Practiced using functions to avoid repeating validation code
- Tested all validation changes successfully

### Day 13

- Created a reusable `find_student()` function
- Used `find_student()` in Search Student
- Used `find_student()` in Update Student
- Used `find_student()` in Delete Student
- Removed repeated student-search loops from the program
- Improved Delete Student to ask again when an invalid Student ID is entered
- Tested Add, View, Search, Update, and Delete operations successfully

### Day 14

- Refactored the Student Management System using functions
- Created `add_student()` for adding students
- Created `view_students()` for displaying students
- Created `search_student()` for searching students
- Created `update_student()` for updating student details
- Created `delete_student()` for deleting students
- Created `display_student()` to avoid repeated student display code
- Reused `find_student()` across Search, Update, and Delete
- Reused phone and email validation functions
- Simplified the main menu to call dedicated functions
- Tested the complete Student Management System after refactoring

### Day 15

- Added reusable `get_valid_name()` function
- Added name validation to prevent empty or space-only names
- Added reusable `get_valid_age()` function
- Added age range validation (5–100)
- Added reusable `get_valid_course()` function
- Added course validation to prevent empty or space-only courses
- Added reusable `get_valid_text()` function for Guardian Name and Address
- Improved email validation using `startswith()` and `endswith()`
- Improved Student ID validation to reject empty or space-only IDs
- Reused validation functions in both Add Student and Update Student
- Added custom prompts for Add and Update operations
- Improved Search, Update, and Delete to handle an empty student list
- Reused `find_student()` for duplicate Student ID checking
- Improved overall input validation and program reliability
- Tested all menu options and validation cases successfully

## Technologies

- Python
- Object-Oriented Programming(OOP)

## Status

- Terminal version completed
- SQLite database integration planned next
- Project in Progress
