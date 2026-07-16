# student data
student = input("please enter the full name of student")

subject_1=int(input("enter the marks of maths ",student," obtain"))
subject_2=int(input("enter the science of maths ",student," obtain"))
subject_3=int(input("enter the marks of english ",student," obtain"))

# date of birth of student
year =int (input("enter the birth date of student"))

subjects = [subject_1,subject_2,subject_3]
total_marks = sum(subjects)

average = total_marks/len(subjects)

age =(2026-year)

authorized_teachers = ('izhar','ubaid','yaseen','umair')
teachers_names =(input("what is the name of teacher"))
if teachers_names.title() in authorized_teachers:
    # student personal details
    print(f"welcome Mr.{teachers_names.title()}! the student result is below")
    print('Student name : ',student)
    print('total marks obtained : ',total_marks)

    # grades of students
    if average >= 90:
        print(f"{student} got grade A (excellent)")
    elif average >= 70 and average < 90:
        print(f"{student} got grade B (very good)")
    elif average >= 50 and average < 70:
        print(f"{student} got grade C (good)")
    else:
        print(f"{student} got grade F (very bad)")

        if age <15:
            print("This is an early-stage failure, provide extra counseling.")
        else:
            print("last warning next time leave the school")

    print(student,' is : ',age,'year old')
else:
    print("you are not an authorized authorized teahcer")






