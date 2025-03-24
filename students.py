import os

def load_students(filename="students.txt"):
    students = {}
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 4:
                    sid, name, gpa, year = parts
                    students[sid] = {"name": name, "gpa": float(gpa), "year": int(year)}
    return students

def save_students(students, filename="students.txt"):
    with open(filename, "w", encoding="utf-8") as file:
        for sid, data in students.items():
            file.write(f"{sid},{data['name']},{data['gpa']},{data['year']}\n")

def add_student(students):
    sid = input("Enter student ID: ")

    if sid in students:
        print("Student already exists.")
        return
    name = input("Enter student name: ")
    gpa = float(input("Enter student GPA: "))
    year = int(input("Enter student year of study: "))

    students[sid] = {"name": name, "gpa": gpa, "year": year}

    print(f"Student {name} added successfully.")
    save_students(students)

def search_student(students):
    search_term = input("Enter ID or part of name to search: ").lower()

    found = False
    for sid, data in students.items():
        if search_term in sid.lower() or search_term in data['name'].lower():
            print(f"Student ID: {sid}\nName: {data['name']}, {data['gpa']}, {data['year']}")
            found = True
    if not found:
        print("Student not found.")

def display_students(students):
    print("\nID | Name | GPA | Year")
    print("-" * 40)
    for sid, data in students.items():
        print(f"{sid} | {data['name']} | {data['gpa']} | {data['year']}")

def main():
    students = load_students()

    while True:
        print("\n1. Add new student")
        print("2. Search student")
        print("3. Display all students")
        print("0. Exit")
        choice = input("Select action (0-3): ")

        if choice == "1":
            add_student(students)
            save_students(students)
        elif choice == "2":
            search_student(students)
        elif choice == "3":
            display_students(students)
        elif choice == "0":
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Try again.")
