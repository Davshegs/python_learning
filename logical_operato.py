# Check if a user's name is not empty and the age is greater than or equal to 18

usersname = input("Enter your username:")
age = int(input("Enter Your age:"))
print(usersname and age >= 18)

# Check if the password is at least 8 character long and does not contain spaces

password = input("Enter password: ")
print((len(password) >= 8) and (password == password.strip()))

# Check if a user's email is not empty, contains '@' and ends with '.com'

email = input("Enter email:")
print(not(email))


# Check is a username is s string, is not None, and is longer than 5 characters
# Check if the user is either an admin or a moderator, and either they're not banned or 
# they're not banned or they've verified their email.
