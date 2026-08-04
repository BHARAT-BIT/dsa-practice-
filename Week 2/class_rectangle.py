class Rectangle:
    def __init__(self, width , height,  ):
        self.width = width 
        self.height= height 
      

    @property 
    def area(self):
        return self.__width * self.__height 
     
    @property
    def values(self):
        return self.__width , self.__height

    @values.setter
    def values(self, width , height):
        if width <=0 or height <=0:
            raise ValueError("Width or Height Can be negative or zero ")
        self.__width = width 
        self.__height = height 

    def __str__(self):
        return f"Rectangle ({self.width} * {self.height})"
    
    def __eq__(self, other):
        return self.area == other.area 
        
rect1 = Rectangle(10 , 30 )
rect2 = Rectangle (15 , 20 )
print(rect1.area)
rect1.values = 5 , 10 
print(rect1)
print(rect1 == rect2)