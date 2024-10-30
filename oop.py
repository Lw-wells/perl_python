class Fruits:
    #constructor method
    def __init__(self,name,price,color):
        self.name=name
        self.price=price
        self.color=color

        #method
    def display(self):
        print(f"I love eating {self.name}, it costs {self.price} and it is {self.color} in color")

#instance (object.)
myobj=Fruits("apple","Ksh. 20","red")
myobj.display()

myobj2=Fruits("banana","Ksh. 20","yellow")
myobj2.display()
