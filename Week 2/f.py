class Student:
    def __init__(self, marks):
        self.marks=marks 

    @property
    def marks(self):
        return self.__marks

    @marks.setter
    def marks(self,value):
        if value <0 or value > 100:
            raise ValueError("Marks can't be negative or more than 100")
        self.__marks= value 

exam = Student(75)
print(exam.marks)
exam.marks = 88
# exam.marks = 111
print(exam.marks)