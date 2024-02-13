class Fruits:
    def __init__(self,name,price):
        self.name = name
        self.price =price

    def show(self):
      print(f"i like eating {self.name} and it is sold at "
                  f"{self.price}")
myobj=Fruits("apple",30)
myobj.show()
myobj2=Fruits("banana",20)
myobj2.show()
myobj3=Fruits("pinapple",50)
myobj3.show()
myobj4=Fruits("mango",50)
myobj4.show()
myobj5=Fruits("peas",40)
myobj5.show()