import json
import os

# ==================== Functions ====================

def save_data(data):
    with open("students.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def load_data():
    if os.path.exists("students.json"):
        with open("students.json", "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def show_banner():
    print("")
    print("#     #     ooooo      #        #           ooooo")
    print("#     #    o     o     #        #          o     o")
    print("#######   o ======o    #        #         o       o")
    print("#     #   o            #        #         o       o")
    print("#     #    o           #        #          o     o")
    print("#     #     oooooo     ######   ######      ooooo")
    print("")
    print("welcome to 96-DOS")
    print("")

def show_goodbye():
    print("")
    print (" oooooo      ooooo       ooooo     ======o          ##     #     #")
    print(" o           o     o     o     o    |      o        #  #     #   #")
    print("o           o       o   o       o   |==== o        #   #      # #")
    print("o       O   o       o   o       o   |==== o       ######       #")
    print(" o      O    o     o     o     o    |      o     #     #       #")
    print("  oooooo      ooooo       ooooo     ======o     #      #       #")
    print("")
    print("")

def show_all(students):
    if not students:
        print("No students registered")
        return
    for name, info in students.items():
        print(f"Name: {name} | Age: {info['age']} | Grades: {info['grades']}")

def show_student(students, name):
    if name in students:
        info = students[name]
        print(f"Name: {name}")
        print(f"Age: {info['age']}")
        print(f"Grades: {info['grades']}")
    else:
        print("Student not found")

# ==================== Data ====================

students = load_data()

# ==================== Banner & Password ====================

show_banner()

passa = input("Enter password >_ : ")

while passa != "0000":
    print("Invalid password")
    passa = input("Enter password >_ : ")

# ==================== Main Loop ====================

while True:
    cmd = input("> ").strip()

    # ---------- Show all ----------
    if cmd == "stuls":
        show_all(students)

    # ---------- Show one student ----------
    elif cmd == "stun":
        name = input("stu name > ").strip()
        show_student(students, name)

    # ---------- Add student ----------
    elif cmd == "add stu":
        name = input("New student name > ").strip()
        if name in students:
            print("Name already exists")
        else:
            age = input("Age > ").strip()
            students[name] = {"age": age, "grades": []}
            save_data(students)
            print(f"Student {name} added")

    # ---------- Delete student ----------
    elif cmd == "del stu":
        name = input("Student name > ").strip()
        if name in students:
            del students[name]
            save_data(students)
            print(f"Student {name} deleted")
        else:
            print("Student not found")

    # ---------- Rename student ----------
    elif cmd == "edit stu":
        old_name = input("Old name > ").strip()
        if old_name in students:
            new_name = input("New name > ").strip()
            if new_name in students:
                print("Name already exists")
            else:
                students[new_name] = students.pop(old_name)
                save_data(students)
                print(f"{old_name} renamed to {new_name}")
        else:
            print("Student not found")

    # ---------- Add grade ----------
    elif cmd == "add nomre":
        name = input("Student name > ").strip()
        if name in students:
            try:
                grade = int(input("Grade > ").strip())
                students[name]["grades"].append(grade)
                save_data(students)
                print(f"Grade {grade} added for {name}")
            except ValueError:
                print("Grade must be a number")
        else:
            print("Student not found")

    # ---------- Edit grade ----------
    elif cmd == "edit nomre":
        name = input("Student name > ").strip()
        if name in students:
            try:
                index = int(input("Grade index (from 0) > ").strip())
                new_grade = int(input("New grade > ").strip())
                students[name]["grades"][index] = new_grade
                save_data(students)
                print("Grade updated")
            except ValueError:
                print("Invalid input")
            except IndexError:
                print("This grade index does not exist")
        else:
            print("Student not found")

    # ---------- Delete grade ----------
    elif cmd == "del nomre":
        name = input("Student name > ").strip()
        if name in students:
            try:
                index = int(input("Grade index (from 0) > ").strip())
                removed = students[name]["grades"].pop(index)
                save_data(students)
                print(f"Grade {removed} deleted")
            except ValueError:
                print("Invalid input")
            except IndexError:
                print("This grade index does not exist")
        else:
            print("Student not found")

    # ---------- Exit ----------
    elif cmd == "exit":
        gfgf = input("exit(y/n) > ").strip()
        if gfgf == "y":
            save_data(students)
            show_goodbye()
            break

    # ---------- Help ----------
    elif cmd == "help":
        print("Available commands:")
        print("  stuls        - Show all students")
        print("  stun         - Show one student")
        print("  add stu      - Add new student")
        print("  del stu      - Delete student")
        print("  edit stu     - Rename student")
        print("  add nomre    - Add grade")
        print("  edit nomre   - Edit grade")
        print("  del nomre    - Delete grade")
        print("  exit         - Exit")

    # ---------- Invalid command ----------
    else:
        print("Invalid command. Type 'help' for help")
