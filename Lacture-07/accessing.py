student = {"name": "Alice", "age": 25, "grade": "A", "major": "Computer Science"}

for key in student :
    print(f"{key}: {student[key]}")

for value in student.values():
    print(value)

for key, value in student.items():
    print(f"{key}: {value}")