# Student Database Program
# Team Final Project
#Josiah Hendley, Nicholas Kavanagh

students = []


# Function to add a student
def add_student():
    print("\nEnter Student Information")

    student_id = input("Student ID: ")
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    age = input("Age: ")
    major = input("Major: ")
    gpa = input("GPA: ")
    email = input("Email: ")
    graduation_year = input("Graduation Year: ")

    student = {
        "StudentID": student_id,
        "FirstName": first_name,
        "LastName": last_name,
        "Age": age,
        "Major": major,
        "GPA": gpa,
        "Email": email,
        "GraduationYear": graduation_year
    }

    students.append(student)
    print("\nStudent added successfully!\n")


# Function to display all students
def view_students():
    if len(students) == 0:
        print("\nNo students in database.\n")
        return

    print("\nStudent Database")
    print("-" * 50)

    for student in students:
        print(f"Student ID: {student['StudentID']}")
        print(f"First Name: {student['FirstName']}")
        print(f"Last Name: {student['LastName']}")
        print(f"Age: {student['Age']}")
        print(f"Major: {student['Major']}")
        print(f"GPA: {student['GPA']}")
        print(f"Email: {student['Email']}")
        print(f"Graduation Year: {student['GraduationYear']}")
        print("-" * 50)


# Function to search for a student
def search_student():
    search_id = input("\nEnter Student ID to search: ")

    for student in students:
        if student["StudentID"] == search_id:
            print("\nStudent Found")
            print("-" * 50)
            print(f"Student ID: {student['StudentID']}")
            print(f"First Name: {student['FirstName']}")
            print(f"Last Name: {student['LastName']}")
            print(f"Age: {student['Age']}")
            print(f"Major: {student['Major']}")
            print(f"GPA: {student['GPA']}")
            print(f"Email: {student['Email']}")
            print(f"Graduation Year: {student['GraduationYear']}")
            print("-" * 50)
            return

    print("\nStudent not found.\n")


# Function to edit a student record
def edit_student():
    edit_id = input("\nEnter Student ID to edit: ")

    for student in students:
        if student["StudentID"] == edit_id:
            print("\nLeave blank to keep current value.\n")

            first_name = input(
                f"First Name ({student['FirstName']}): ")
            if first_name != "":
                student["FirstName"] = first_name

            last_name = input(
                f"Last Name ({student['LastName']}): ")
            if last_name != "":
                student["LastName"] = last_name

            age = input(
                f"Age ({student['Age']}): ")
            if age != "":
                student["Age"] = age

            major = input(
                f"Major ({student['Major']}): ")
            if major != "":
                student["Major"] = major

            gpa = input(
                f"GPA ({student['GPA']}): ")
            if gpa != "":
                student["GPA"] = gpa

            email = input(
                f"Email ({student['Email']}): ")
            if email != "":
                student["Email"] = email

            graduation_year = input(
                f"Graduation Year ({student['GraduationYear']}): ")
            if graduation_year != "":
                student["GraduationYear"] = graduation_year

            print("\nStudent record updated successfully!\n")
            return

    print("\nStudent not found.\n")


# Function to delete a student
def delete_student():
    delete_id = input("\nEnter Student ID to delete: ")

    for student in students:
        if student["StudentID"] == delete_id:
            students.remove(student)
            print("\nStudent deleted successfully.\n")
            return

    print("\nStudent not found.\n")


# Main program loop
while True:
    print("\n===== Student Database Menu =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Edit Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        edit_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        print("\nExiting program...")
        break

    else:
        print("\nInvalid choice. Please try again.")
