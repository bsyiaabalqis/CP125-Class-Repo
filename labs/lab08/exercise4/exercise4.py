# Lab 08 Exercise 4: Student Grade Calculator
# Write your code below:
import csv 
def calculate_final_grades(input_file, output_file):
    input = open(input_file, "r", newline= "")
    reader = csv.reader(input) 

    output = open(output_file, "w", newline= "")

    """
    Calculate final grades from midterm and final scores.

    Args:
        input_file: path to scores CSV (student_id,midterm,final)
        output_file: path to output CSV file

    Returns: 
        float: average of all final grades
    """

result = calculate_final_grades("/labs/lab08/exercise4.py/data/scores.csv", "/labs/lab08/exercise4.py/data/grades.csv")
print(f"Average final grade: {result:.2f}")
