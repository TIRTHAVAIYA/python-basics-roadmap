class Car:
    def __init__(self , make , model , year):
        self.make = make
        self.model = model
        self.year = year
        self.is_running = False

    def start(self):
        if not self.is_running:
            self.is_running = True
            print(f"The {self.year} {self.make} {self.model} has started.")    
        else:
            print(f"The {self.year} is already running.")

    def stop(self):
        if self.is_running:
           self.is_running = False
           print(f"The {self.model} has stopped.")
        else:
             print (f"The {self.model} is already stopped.")   
  
### CREATING AN OBJECT....

my_car = Car("TOYOTA" , "CAMRY" , 2022)

## CAll the methods

my_car.start()
my_car.stop()

    