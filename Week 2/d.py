class Bird:
    def fly(self):
        print("Birds fly high.")
class Penguin(Bird):
    def fly(self):
        print("Penguins cannot fly, it swims instead.")
class Sparrow(Bird):
    def fly(self):
        super().fly()        

b1 = [Bird(), Penguin(), Sparrow()]     
for bird in b1:
    bird.fly()
