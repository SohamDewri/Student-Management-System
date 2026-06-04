# Student Management System

students = {}

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        roll_no = input("Enter Roll Number: ")
        name = input("Enter Student Name: ")
        students[roll_no] = name
        print("Student added successfully!")

    elif choice == "2":
        if len(students) == 0:
            print("No student records found.")
        else:
            print("\nStudent Records:")
            for roll_no, name in students.items():
                print(f"Roll No: {roll_no}, Name: {name}")

    elif choice == "3":
        roll_no = input("Enter Roll Number to Search: ")
        if roll_no in students:
            print(f"Student Found: {students[roll_no]}")
        else:
            print("Student not found.")

    elif choice == "4":
        roll_no = input("Enter Roll Number to Delete: ")
        if roll_no in students:
            del students[roll_no]
            print("Student deleted successfully!")
        else:
            print("Student not found.")

    elif choice == "5":
        print("Thank you for using Student Management System.")
        break

    else:
        print("Invalid choice! Please try again.")
