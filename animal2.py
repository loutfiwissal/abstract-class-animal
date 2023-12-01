from abc import ABCMeta , abstractmethod

class animal (metaclass = ABCMeta) :
    def __init__(self,name,age,race,color):
        self._name = name
        self._age = age
        self._race = race
        self._color = color


    @property
    def getname (self):
        return self._name
    
    @property
    def getage (self):
        return self._age
    
    @property
    def getrace (self):
        return self._race
    
    @property
    def getcolor (self):
        return self._color
    
    def setname (self,name) :
        self._name= name
    def setage (self,age) :
        self._age = age
    def setrace (self,race) :
        self._race = race
    def setcolor (self,color) :
        self._color = color

    def run (self):
        print (f"the animal {(self._name)} runing")

    @abstractmethod
    def sound (self):
        pass

 
# the child class 
class horse (animal) :
    def __init__(self,name,age,race,color):
        super().__init__(name,age,race,color)
        

    def info (self):
        print(f"the name :{self.getname}")
        print (f"the age:{self.getage}")
        print (f"the race :{self.getrace}")
        print (f"the color:{self.getcolor}")

    def jump (self) :
       print (f"the animal{(self.getname)} jump")

    def sound (self) :
        print ("henessement")


class cat (animal):
    def __init__(self,name,age,race,color,food):
        super().__init__(name,age,race,color)
        self.food=food

    def eat (self):
        print(f"{self.getname} eat {self.food}")
    def sound(self):
        print ("myaw")
    def play (self):
        print(f"{self.getname} play")

    
#main programme
h1 = horse ("jack","21","arabi","black")
h1.info()
h1.jump()
h1.sound()






