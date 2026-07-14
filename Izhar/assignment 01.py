# student details
name = input("what is your name?")
age = input("what is your age?")
adress = input("what is your adress?")
phone = input("what is your phone?")


print("my name is " + name)
print("my age is " + age)
print("my adress is " + adress)
print("my phone number is " + phone)

print("and my marks is")
# student mark sheet
total_marks = 500
print("the total marks = ",total_marks)
# per paper marks
print("marks per paper is 100")

# paper marks out of 100
physics = int(input("marks in physics = "))
math =    int(input("marks in maths = "))
islamic_studies = int(input("marks in islamic_studies = "))
urdu =    int(input("marks in urdu = "))
english = int(input("marks in english = "))

# full result sum of obtain marks
obtain_marks = physics+math+islamic_studies+urdu+english

print(obtain_marks,"/",total_marks)

# percentage
percentage = obtain_marks/total_marks*100

print(percentage,"%")

# average marks
average_marks = obtain_marks/5
print("the average mark is = ",average_marks)