class Student:
    school_name = "ABC School"

    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number

    def display(self):
        print(f"{self.name} (Roll No: {self.roll_number}) studies at  {Student.school_name}.")

s1=Student("Alice", 101)
s2=Student("Bob", 102)
s3=Student("Charlie", 103)
s1.display()
s2.display()    
s3.display()