class Student:
    def __init__(self , name):
        self.name = name
        self.marks = []

    def add_mark(self,mark):
        if 0 <= mark <=100 :
            self.marks.append(mark)
            print(f"Mark {mark} added for {self.name}")
        else:
            print("Inva;lid mark")   

    def calc_grade(self):
        if not self.marks:
            return f"{self.name} has no recorded"
        
        average = sum(self.marks) / len(self.marks)

        if average >= 90:
            grade = 'A'
        elif average >= 80:
            grade = 'B'   
        elif average >= 70:
            grade = 'C' 
        elif average >= 60:
            grade = 'D'  
        else:
            grade = 'F'            
        return f"{self.name}'s average is {average: .2f} , Grade : {grade}"
    

## CREATING OBJECTS
student1 = Student("TIRTH")
student1.add_mark(95)
student1.add_mark(93)
student1.add_mark(90)

print(student1.calc_grade())

    