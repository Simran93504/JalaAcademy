print("Print gender (Male/Female) program according to given M/F using switch")

def print_male():
    print("Male")

def print_female():
    print("Female")

gender = input("Enter gender (M/F): ")

switcher = {
    'M': print_male,
    'm': print_male,
    'F': print_female,
    'f': print_female,
}

switcher.get(gender, lambda: print("Invalid input."))()
