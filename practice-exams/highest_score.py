student_marks = {
    'Jack': 78,
    'Amy': 90,
    'Bob': 67,
    'Harry': 93
}

scores = student_marks.values()
highest_score = max(scores)

for name, score in student_marks.items():
    if score == highest_score:
        best_student = name

print(f"{best_student} scored {highest_score}")
