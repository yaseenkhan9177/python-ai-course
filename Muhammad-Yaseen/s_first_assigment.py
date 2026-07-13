#  sir g assigment
name = str(input("Enter your name: "))
age = int(input("Enter your age:"))
address = str(input("Enter your address:"))
math = int(input("Enter your math marks :" ))
english = int(input("Enter your english marks :" ))
physics = int(input("Enter your Physics marks :" ))
urdu =  int(input("Enter your Urdu marks :" ))
islamic_s =  int(input("Enter your Islamic_studies marks :" ))

#for bio
print(f"Hi {name}! You are from {address} and your age is {age}.")
#maks
print(f"Math: {math}, English: {english}, Physics: {physics}, Urdu: {urdu}, Islamic Studies: {islamic_s}")

obtained_marks =  (english + math + physics + urdu +islamic_s)
total_marks = 500
# print total marks
print(f"total marks is {obtained_marks}/{total_marks}")
#Percentage Calculation
print(f"percentage ={(obtained_marks / total_marks)*100}%")
#Average Calculation
print(f"average marks is {obtained_marks/5}")


