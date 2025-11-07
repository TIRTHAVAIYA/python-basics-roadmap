## POLYMORPHISM.....

class Cat:
    def speak(self):
        return "Meow!!!"


class Duck:
    def speak(self):
        return "Quack!!!"
    

class Person:
    def speak(self):
        return "Hello!!!"    
    

def make_it_speak(entity):
    print(entity.speak())    

cat = Cat()
duck = Duck()
person = Person()

print("Demonstrating Polymorphism: ")
make_it_speak(cat)
make_it_speak(duck)
make_it_speak(person)

