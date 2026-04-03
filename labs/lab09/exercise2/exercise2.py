import pandas as pd


def compare_averages(filename):
    df = pd.read_csv("labs/lab09/data/students.csv")

    # calculate mean for 3 subjects
    mean_math = df["Math"].mean()
    mean_science = df["Science"].mean()
    mean_english = df["English"].mean() 

    # store 3 subjects in a dict
    average = { "Math": mean_math, "Science": mean_science, "English": mean_english}
    
    # identify best n worst subjects 
    best = max(average, key=average.get)
    worst = min(average, key= average.get)

    result = {
        "Math": mean_math ,
        "Science": mean_science, 
        "English": mean_science, 
        "best_subject": best, 
        "worst_subject": worst  
    }
