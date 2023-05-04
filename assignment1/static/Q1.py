class MyClass:
    static_var = 0
    
    @classmethod
    def class_method(cls):
        print("Class method called.")
        print(f"Static variable value: {cls.static_var}")
        
    @staticmethod
    def static_method():
        print("Static method called.")
        print(f"Static variable value: {MyClass.static_var}")

MyClass.class_method()   # Output: Class method called. Static variable value: 0
MyClass.static_method()  # Output: Static method called. Static variable value: 0
