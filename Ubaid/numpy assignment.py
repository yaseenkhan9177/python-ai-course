import pandas as pd

text =[78,85,92,67,88]
data = pd.Series(text)
print(data)

students ={ "name" : ["ali","ahmad","hamza","bilal","usman"],
            "age" : [20,21,20 ,22,21],
            "marks" : [78,85,92,67,88],
            "city" : ["swat","peshawar","mingora","islamabad","lahore"]
            }
result = pd.DataFrame(students,index = ["students1","students2","students3","students4","students5"])
print(result)

print(result.loc["students1"])
print(result.loc["students3"])
print(result.loc[["students1","students4"]])
print(result.loc[["students2","students3","students5"]])


record= pd.read_csv("students.csv")
print(record)

import numpy as np

text = [10,20,30,40,50]
data = np.array(text)
print(data)
print (text[0])
print(text[4])


# 2y dimension array
text2 = np.array ([[10,20,30],[40,50,60],[70,80,90]])
print(text2)
print("--first row---------------")
print(text2[0])

print("-second row----------------")
print(text2[1])

print("--the value of-----------------")
print(text2[1][1])

# task 8
# mini project
students = {
    "names" : ["ubaid","sahil","izhar","umair","yseen","wajid","rahman","asad"],
    "age" : [20,30,24,23,21,26,27,28],
    "marks" : [78,85,92,67,88,67,78,90],
    "city" : ["kalm","madyn","bahran","malmjabba","mingora","kabal","sigram","kanju"]
}

stdname = pd.DataFrame(students,index=["student1","student2","student3","student4","student5","student6","student7","student8"])
print(stdname)

print(stdname.loc["student1"])
print(stdname.loc[["student2","student3"]])
print(stdname.loc[["student4","student5","student6"]])

readfile = pd.read_csv("students.csv")
print(readfile)

array = np.array([["std1","std2","std3","std4"],[80,90,70,85],[75,88,65,80],[85,92,78,90]])

print(f"the first student pythonmarks is {array[1,0]} math mark is {array[2,0]} english marks is {array[3,0]}")
print(array)
print(array[0])

print(f"math mark of all std  is {array[2]} ")

print(f"std3 english marks is {array[3,2]}")
