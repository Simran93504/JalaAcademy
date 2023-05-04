print("Define a static variable and change within the class")
class MyClass:
    static_var = 0
    
    def method(self):
        print("Instance method called.")
        print(f"Static variable value: {MyClass.static_var}")
        
MyClass.static_var = 1
my_object = MyClass()
my_object.method()  # Output: Instance method called. Static variable value: 1
MyClass.static_var = 2
my_object.method()  # Output: Instance method called. Static variable value: 2
