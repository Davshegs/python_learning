# Write a Python script that prompts for a student's name and last exam grade.
#  Add 50 to their score, and divide their score by 4. Save the result. 
# Then print their name and their result

student_name = input("Enter your name: ") 
last_exam_grade = float(input("Enter your last exam grade: "))
result = (last_exam_grade + 50) / 4
print(f"{student_name} : {result}")