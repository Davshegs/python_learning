# You are going to get input from a student. And then tell them their class of grade. 
# Ensure that you are able to filter out wrong input

# 3.5- 4.00 – First Class Honours
# 3.0-3.49 – Second Class Honours (Upper Division)
# 2.0-2.99 – Second Class Honours (Lower Division)
# 1.0-1.99 – Third Class Honours

student_grade = float(input("Enter your grade:"))

if  student_grade >= 3.5 and student_grade <= 4.0:
    print("First Class Honours")
elif student_grade >= 3.0 and student_grade <= 3.49:
    print("Second Class Honours (Upper Division)")
elif student_grade >= 2.0 and student_grade <= 2.99:
    print("Second Class Honours (Lower Division)")
elif student_grade >= 1.0 and student_grade <= 1.99:
    print("Third Class Honours")
else:
    print("Invalid grade")