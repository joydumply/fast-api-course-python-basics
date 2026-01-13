"""
String Formatting in Python
"""

first_name = "Nik"

print("Hello, " + first_name + "!")  # Concatenation
print(f"Hello, {first_name}!")  # f-string

sentence = "Hi {} {}!"
last_name = "Babichev"
print(sentence.format(first_name, last_name))  # str.format() method