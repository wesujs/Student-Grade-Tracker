
# Student Grade Tracker
This is a python script that allows users to manage and track the grades of students. The script offers a user interface that allows users to add, remove, and view the grades of individual students or all students. The script also offers an option to delete all student grades, and an option to exit the program.

## How to use
To use the script, run it in a python interpreter. The user will be prompted with a menu of options. Select an option by entering the corresponding number.

### Add Student: 

Allows the user to add a new student to the system. The user will be prompted to enter the student's name, and then enter the student's grades one by one. To finish adding grades, the user must enter 'done'.

### Remove Student:

Allows the user to remove a student from the system. The user will be prompted to enter the student's name. If the student is found in the system, their grade file will be removed.

### View Grades for a student: 

Allows the user to view the grades of an individual student. The user will be prompted to enter the student's name. If the student is found in the system, their grades will be displayed.

### View Grades for all students: 

Allows the user to view the grades of all students in the system. If there are no students in the system, a message will be displayed stating so.

### Delete All Student Grades: 

Allows the user to delete all student grades in the system. This action cannot be undone.

### Exit: 

Exits the program.

## Notes
The script stores the student data in a text file called 'students.txt'. The data is stored as a list of tuples, with each tuple representing a student's name, grades, and average grade.
The script calculates and displays the letter grade for each student, using a conversion dictionary. The conversion is based on the following scale:
A: 90% and above
B: 80% - 89%
C: 70% - 79%
D: 60% - 69%
F: Below 60%
