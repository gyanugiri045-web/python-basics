students = []

def add_student():
    try:
        name = input("Enter student name:")
        roll = int(input("Enter student rollno:"))
        marks = []

        print("Enter 5 subject:")

        for i in range(5):
            mark = int(input(f"subject {i + 1}:"))
            marks.append(mark)

        new_student = {
            "name": name,
            "roll": roll,
            "marks": marks
        }

        students.append(new_student)

        print("Student added successfully!!")

    except ValueError:
        print("please enter number only!!")


def view_students():
    if len(students) == 0:
        print("Invalid number!!")
        return

    for student in students:
        print("\nStudent Name:", student["name"])
        print("Roll Number:", student["roll"])
        print("Marks:", student["marks"])


def calculate_average():
    for student in students:
        marks = student["marks"]
        total = sum(marks)
        percentage = total / 500 * 100

        if percentage >= 90:
            grade = "A+"
        elif percentage >= 80:
            grade = "A"
        elif percentage >= 70:
            grade = "B+"
        elif percentage >= 60:
            grade = "B"
        elif percentage >= 50:
            grade = "C+"
        else:
            grade = "fail"

        print("\nName:", student["name"])
        print("Total marks:", marks)
        print("Percentage:", percentage)
        print("Grade:", grade)



def save_to_file():

    try:
        file = open("students.txt", "a")

        for student in students:

            file.write(str(student) + "\n")


        file.close()

        print("Data saved successfully")

    except Exception:
        print("Error while saving file")

def load_from_file():
    try:
        file = open("students.txt", "r")

        for line in file:
            print(line)

        file.close()

    except FileNotFoundError:
        print("File not found")


add_student()
view_students()
calculate_average()
save_to_file()
load_from_file()                                                                                                                                                   
