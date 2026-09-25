def calculate_grade(average):
    if 70 < average <= 100:
        grade = "A"
    elif 60 < average < 69:
        grade = "B"
    elif 50 < average < 59:
        grade = "C"
    elif 40 < average < 44:
        grade = "D"
    else:
        grade = "F"
    return grade

name = input("Enter student name: ")
 
marks1 = float(input("Enter marks for Subject 1: "))
marks2 = float(input("Enter marks for Subject 2: "))
marks3 = float(input("Enter marks for Subject 3: "))
marks4 = float(input("Enter marks for Subject 4: "))
marks5 = float(input("Enter marks for Subject 5: "))
 
total = marks1 + marks2 + marks3 + marks4 + marks5
average = total / 5
grade = calculate_grade(average)
 
print(f"""
Name : {name}
Total Marks: {total}
Average: {average}
Grade: {grade}
""")
 