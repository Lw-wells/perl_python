#a class of person with the following; name , age and gender as the attribute
#a constructor , a method and an object
from oop import myobj


class Student:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
            #METHOD
    def display(self):
        print(f"My name is {self.name}, I am {self.age} of age  and I am a {self.gender}")

#OBJECT
myStudent=Student("Wells",20,"male")
myStudent.display()