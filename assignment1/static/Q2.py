print("Define a static variable and access that through a instance")

class MyClass:
    static_var = 0
    
    def __init__(self):
        self.instance_var = 0
        
    def method(self):
        print("Instance method called.")
        print(f"Static variable value: {self.static_var}")
        print(f"Instance variable value: {self.instance_var}")
        
my_object = MyClass()
my_object.method()  # Output: Instance method called. Static variable value: 0. Instance variable value: 0
