# Write a simple Python program that takes a person's name as input and greets them. 
#Write a simple Python program that takes a person's name and age as input. Then welcome the page and their age plus 20
# Hint: 
# Make sure all the collected input is stored as a variable.
# Any little computation should be stored as a variable

name = input("Enter your name: ")

print("Good Evening", name)

age = int(input("Enter your age:"))
additional_age = age + 20
print(f"Good evening {name}, you are {additional_age} years old")


