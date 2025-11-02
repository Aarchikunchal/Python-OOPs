#intiate a class 
class employee:
    #special method/magic method/duder method - constructor
    def __init__(self):
        print("Started executing attributes/data")
        self.id=123
        self.salary=50000
        self.designation="SDE"
        print("attributes and data have been initiated")
    #method 
    def travel(self,destination):
        print("this travel method was called manually")
        print(f"Employee is now travelling to {destination}")
    
#creating an obj/instance
sam=employee()
#calling a method
sam.travel("new york")
print(type(sam))

