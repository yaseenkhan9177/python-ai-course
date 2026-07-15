# Access control
allowed_user=("izhar","umair","yaseen","ubaid")
names=input("enter your name;")
if names in allowed_user:
    print(f"access granted:welcome! {names};")
else:
    print("access denied:you are not authorized")
age = int(input("enter your age;"))

if age>=18:
    print("you are old enough to enter")
else:
    print("sorry you must be 18 to enter")
    


