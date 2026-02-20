# Given the list below
# sales = [120,450,800,50,900,300]
# Write a Python code that classifies items in the list as Low, Medium, or High. 
# Also, do a count of items based on this classification and finally give a sum of items in each classification
# Key: less than 300 – low
#        > 300 <= 700 medium
# > 700 that's high



sales = [120, 450, 800, 50, 900, 300]
low = 0
medium =0
high = 0
for item in sales:
    if item <= 300:
        low += 1
    elif 300 < item <= 700:
        medium += 1
    else:
        high += 1
print("Total low sales:", low)
print("Total medium sales:", medium)
print("Total high sales:", high)


# From temperatures = [30,22,35,19,40], print those above average.

temperatures = [30,22,35,19,40]
sum_temp = sum(temperatures)
avg_temp = sum_temp / len(temperatures)
print("The average temperature is:", avg_temp)


# Given numbers = [12, 7, 9, 20, 33, 14, 5], print only even numbers and store them in a new list.

numbers = [12, 7, 9, 20, 33, 14, 5]
even_num = []
for num in numbers:
    if num % 2 == 0:
        even_num.append(num)
print(even_num)