
# # Simple inheritance
# # Base class
# class Animal:
#     def __init__(self,name):
#         self.name =name
#     def speak(self):
#         print(f"{self.name} makes a sound.")
# # Derived class
# class Dog(Animal):
#     # def __init__(self):
#     #     self.behaviour="friendly"
#     def speak(self):
#         print(f"{self.name} barks")
# # Create an instance of Animal
# # animal = Animal("Generic Animal")
# # animal.speak()  # Output: Generic Animal makes a sound.
# # Create an instance of Dog
# dog = Dog()
# dog.speak() 
# # animal.speak1() cannot access child class attributes and method


# SUPER KEYWORD
class Animal:
    def __init__(self):
        self.name = "Buddy"
        self.age=26

    def speak(self):
        print(f"{self.name} makes a sound.")

# # Derived class
class Dog(Animal):
    def __init__(self, breed):
        super().__init__()
        self.breed = breed

    def speak(self):
        super().speak()
        print(f"{self.name} barks. It is a {self.breed} and his age is {self.age}")

dog = Dog("golden")
dog.speak()



