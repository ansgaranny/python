class Car:
    def __init__(self,make,model,year,color):
        self.make=make
        self.model=model
        self.year=year
        self.color=color
    def onyesha(self):
        print(f"my dream car is {self.make} and my model is {self.model} "
              f"manufactured in {self.year} and color is {self.color}")
myobj=Car("Toyota","Vits",2020,"blue")
myobj.onyesha()

myobj2=Car("Mazda","Bmw",2023,"red")
myobj2.onyesha()
