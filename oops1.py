#intiate a class 
class employee:
    #special method/magic method/duder method - constructor
    def __init__(self):
        print(id(self))
        print("Started executing attributes/data")
        self.id=123
        self.salary=50000
        self.designation="SDE"
        print("attributes and data have been initiated")
    #method 
    def travel(self):
        print("this travel method was called manually")
        # print(f"Employee is now travelling to {destination}")
    
#creating an obj/instance
sam=employee()
print(id(sam))

# sam1=employee()
# print(id(sam1))
sam.name="SAM kumar"
print(sam.name)

#calling a method
sam.travel()
# sam.travel("new york") #by default there is self arguments
# print(type(sam))

