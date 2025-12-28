student_marks = {
    "Alice": 85,
    "Bob": 78,
    "Will": 92,
    "Max": 88
}
name = input("Enter the student's name: ")
if name in student_marks:
    marks = student_marks[name]
    print(f"{name}'s marks: {marks}")
else:
    print("Student not found.")