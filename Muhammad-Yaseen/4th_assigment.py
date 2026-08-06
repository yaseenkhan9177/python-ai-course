# Create a class named Student
class Student:

    # Constructor
    def __init__(self):
        # Private attribute (cannot be accessed directly)
        self.__age = 0

    # Setter method to set the age
    def set_age(self, age):

        # Check if the age is valid
        if age > 0:
            self.__age = age
        else:
            print("Invalid age! Age must be greater than 0.")

    # Getter method to get the age
    def get_age(self):
        return self.__age


# Create an object of Student class
student1 = Student()

# Set the student's age
student1.set_age(20)

# Display the student's age
print("Student Age:", student1.get_age())

# Try an invalid age
student1.set_age(-5)