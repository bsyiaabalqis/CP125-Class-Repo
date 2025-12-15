#BATRISYIA BALQIS BINTI ZALLAMI 
# program that checks the grade for one student 

#function to determine grade based on mark 
def determine_grade(mark): 
    if mark >= 80:
        grade = "A"
    elif mark >= 60: 
        grade = "B"
    elif mark >= 50:
        grade = "C"
    elif mark >= 40: 
        grade = "D" 
    else: 
        grade = "F"
    return grade 

#input mark from user
mark = float(input("Enter the student's mark:"))
grade = determine_grade(mark)
print(f"Mark:{mark}, Grade:{grade}")