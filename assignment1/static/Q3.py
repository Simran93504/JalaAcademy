print("Define a static variable and change within the instance")
class MyClass:
    static_var = 0
    
    def method(self):
        print("Instance method called.")
        print(f"Static variable value: {self.static_var}")
        self.static_var += 1
        print(f"Static variable value after increment: {self.static_var}")
        
my_object = MyClass()
my_object.method()  # Output: Instance method called. Static variable value: 0. Static variable value after increment: 1
my_object.method()  # Output: Instance method called. Static variable value: 1. Static variable value after increment: 2
