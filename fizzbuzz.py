# Write a python program that iterates through integers from 1 to 100. 
# For each multiples of three print "Fizz" instead of the number, 
# For each multiple of five, print "Buzz" 
# For Numbers that are both multiple of three and five print "FizzBuzz"

for i in range(1, 101):
    if (i % 3 == 0) and (i % 5 == 0): # filtering for multiple of both 3 and 5
        print("FizzBuzz")
    elif i % 3 == 0:                  # filtering for multiple of both 3
        print("Fizz")
    elif i % 5 == 0:                  # filtering for multiple of both 5
        print("Buzz")
    else:        
        print(i)