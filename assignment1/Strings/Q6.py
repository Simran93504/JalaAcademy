import re
my_string = "Hello, world!"
result = re.match("Hello", my_string)
print(result) # Output: <re.Match object; span=(0, 5), match='Hello'>
