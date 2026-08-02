class rectangle:
    def __init__(self,width,length):
       self.width = width
       self.length = length


       self.final = length*width



    def __str__(self):
            return f"final value is {self.final}"


class employee:
    def __init__(self, name, salary, emp_id):
        self.name = name
        self.emp_id =emp_id
        self.salary = salary

    def raise_amount (self,amount):
        self.final_salary = self.salary + amount

    def __str__(self):
        return f"employee {self.name} salary is {self.salary} and id is {self.emp_id} and final salary {self.salary+amount}"



x = rectangle (length=int(input("enter the length :")),width=int(input("enter the width :")))
print(x)


name = str(input("enter employee name : "))
salary = int(input("enter employee salary : "))
emp_id =int (input("enter employee id : "))
amount = int(input("enter amount to add the employee salary : "))

employeeobj = employee(name, salary, emp_id)
employeeobj.raise_amount(amount)
print(employeeobj)

#another employee detail

name = str(input("enter employee name : "))
salary = int(input("enter employee salary : "))
emp_id =int (input("enter employee id : "))
amount = int(input("enter amount to add the employee salary : "))

employeeobj2 =employee(name,salary,emp_id,)
employeeobj2.raise_amount(amount)
print(employeeobj2)







