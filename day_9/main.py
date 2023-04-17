# Dictionaries and Nesting
person = {
    "name": "Max", 
    "age": 32
}
print(f"The name is {person['name']} with an age of {person['age']}")

print(person.keys())

person["age"] = 24
print(person.values())

# Exercise -> Grading Program
student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
student_grades = {}

for student_key in student_scores:
    if (student_scores[student_key] >= 91):
        student_grades[student_key] = "Outstanding"
    elif (student_scores[student_key] >= 81):
        student_grades[student_key] = "Exceeds Expectations"
    elif (student_scores[student_key] >= 71):
        student_grades[student_key] = "Acceptable"
    else:
        student_grades[student_key] = "Fail"

print(student_grades)


