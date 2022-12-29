import sys

# Dictionary To Convert integers to Letter Grades
grade_ranges = {
    90: 'A',
    80: 'B',
    70: 'C',
    60: 'D',
    0: 'F'
}

# Function to complete the conversion

def get_letter_grade(conversion):
    
    conversion = int(conversion)
    
    for key in grade_ranges:
        if conversion >= key:
            return grade_ranges[key]

data = []

# An empty list to store all entered student's information
students = []

# An exit flag to use when exiting the program

exit_flag = False

# End Script When Last option is selected
def end_script():
    sys.exit()

while not exit_flag:
    # User Interaction Menu
    print("1. Add Student")
    print("2. Remove Student")
    print("3. View Grades for a student")
    print("4. View Grades for all students")
    print("5. Delete All Student Grades")
    print("6. Exit")
    print()
    
    # User Choice Input Slot
    
    choice = int(input("Enter your choice(e.g: 1): "))
    
    if choice == 1:
        # Add a new student
        name = input("Enter the student's name: ")
        grades = []
        while True:
            grade = input("Enter a grade (enter 'done' when finished): ")
            
            if grade == 'done':
                break
            grades.append(int(grade))
        
        # Calculating an average of all grades
        average_grade = round((sum(grades) / len(grades)), 2)
        
        # Add the student to our student list
        names = name.capitalize()
        students.append((names, grades, average_grade))
        
        # Open the file in read mode
        with open('students.txt', 'r') as f:
            
            # Read the lines of the file into a list
            lines = f.readlines()

            # Remove the first element of the list
            lines = lines[1:]

        # Open the file in write mode
        with open('students.txt', 'w') as f:
            # Write the modified list to the file
            f.writelines(lines)
        
        # Open the file in append mode
        with open('students.txt', 'a') as f:
            # Write the student's data to the file as a string representation of a tuple
            f.write(str(students) + '\n')
                 
    elif choice == 2:
        # Removing Student
        name = input("Enter the student's name: ").capitalize()

        found = False

        for i, student in enumerate(students):
            if student[0] == name:
                student_name = str(student[0])
                # Removes Selected Student from list
                students.pop(i)
                print(student_name + "'s grade file has been removed.")

                # Open the file in write mode
                with open('students.txt', 'a') as f:
                    # Write the updated student list to the file
                    for student in students:
                        f.write(str(data(student)) , '\n')

                found = True

                break

        if not found:
            print("Student not found")

            
    elif choice == 3:
        # View grades for a student
        name = input("Enter the student's name: ")
        
        found = False
        
        for student in students:
            
            if student[0] == name:
                
                letter_grade = str(get_letter_grade(student[-1]))
                percentage = str(student[-1])
                student_name = str(student[0])
                
                print(student_name + "'s grade is " + letter_grade + ": " + percentage + "%")
                
                found = True
                
                break
            
        if not found:
            print("Student not found. Please try again.")

    
    elif choice == 4:
        # View the grades for all students
        if not students:
            print("There are no students in the system yet.")
            
        else:
            for student in students:
            
                letter_grade = str(get_letter_grade(student[-1]))
                student_name = str(student[0])
            
                print(student_name + ": " + letter_grade )
            
    elif choice == 5:
        # Remove all grades
        text = '\033[1mAre you sure you want to delete All of the user data from the \033[22m \033[3mstudents.txt file (e.g: y/n ): \033[23m \033[\033[22m '
        make_sure = input(text)
            
        if make_sure == "y" or make_sure == "yes":
            print("All student grades have been wiped from the file.")
            
            with open('students.txt', 'w') as f:
                # Move to the file pointer to the beginning of the file
                f.seek(0)
                # Delete all data from the file
                f.truncate()
        elif make_sure == "n" or make_sure == "no":
            print("File deletion has been cancelled.")
            
    elif choice == 6:
        
        # End The Program
        print("Thanks for using this script. You can restart by using python grades.py in the command window :)")
        
        end_script()
        
        
    
        
            
                
                
            
            
    



