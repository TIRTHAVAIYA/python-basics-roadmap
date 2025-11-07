class Animal:
    def __init__(self,name):
        self.name = name 

    def speak(self):
        raise NotImplementedError("Subclasss must implement abstract method")    
    
    def eat(self):
        print(f"{self.name} is eating.")

    
    
class Dog(Animal): ## child class inheriting from Animal...
    def __init__(self, name , breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        return f"{self.name} {self.breed} says Woof!!"     
    
## CREAT OBJECT..

generic_animal = Animal("Creature")
my_dog = Dog("MIKE" , "Golden Retriever")    

## CALL METHODS

generic_animal.eat()
print(my_dog.speak())
my_dog.eat()  ## INHERITED FROM ANIMAL
