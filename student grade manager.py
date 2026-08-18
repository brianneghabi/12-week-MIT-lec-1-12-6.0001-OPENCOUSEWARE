# Student Grade Manager

students = {}

print("=== Student Grade Manager ===")

while True:
    print("\nMenu")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Enter student name: ")

        grades = []

        for i in range(3):
            grade = float(input(f"Enter grade {i + 1}: "))
            grades.append(grade)

        average = sum(grades) / len(grades)

        # Tuple stores highest and lowest grade
        high_low = (max(grades), min(grades))

        # Dictionary stores all student information
        students[name] = {
            "Grades": grades,
            "Average": average,
            "Highest and Lowest": high_low
        }

        print(f"{name} has been added.")

    elif choice == "2":
        if len(students) == 0:
            print("No students found.")
        else:
            for name, info in students.items():
                print("\n---------------------")
                print("Name:", name)
                print("Grades:", info["Grades"])
                print("Average:", round(info["Average"], 2))
                print("Highest Grade:", info["Highest and Lowest"][0])
                print("Lowest Grade:", info["Highest and Lowest"][1])

    elif choice == "3":
        search = input("Enter student name: ")

        if search in students:
            info = students[search]
            print("\nStudent Found")
            print("Grades:", info["Grades"])
            print("Average:", round(info["Average"], 2))
            print("Highest Grade:", info["Highest and Lowest"][0])
            print("Lowest Grade:", info["Highest and Lowest"][1])
        else:
            print("Student not found.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")