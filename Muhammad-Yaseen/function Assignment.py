def create_student_profile(s_name, s_age, **student_scores):
    print(f"Student Name: {s_name}")
    print(f"Student Age: {s_age}")

    marks = []

    for subject, mark in student_scores.items():
        print(subject, mark)
        marks.append(mark)

    print(marks)


create_student_profile(
    s_name=str(input("Enter Student Name: ")),
    s_age=int(input("Enter Student Age: ")),
    math_marks=int(input("Enter Student Math Marks: ")),
    english_marks=int(input("Enter Student English Marks: "))
)