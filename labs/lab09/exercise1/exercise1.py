import pandas as pd

def explore_data(filename):
    # loads csv into dataframe
    df = pd.read_csv("labs/lab09/data/students.csv") 

    # calculate required statistics
    total_students = len(df)
    subjects = ["Math", "Science", "English"]

    # average score for math 
    avg_math = df["Math"].mean()

    #highest for math 
    highest_math = df["Math"].max()
    highest_math_student = df.loc[df["Math"] == highest_math, "Name"].iloc[0]

    return { "subjects": subjects, "avg_math": avg_math, "highest_math": highest_math, "highest_math_student": highest_math_student } 