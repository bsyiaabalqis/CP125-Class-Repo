import pandas as pd
import matplotlib.pyplot as plt


def show_science_distribution(filename):
    df = pd.read_csv(filename)

    # create histogram with 10 bins 
    plt.hist(df['Science'], bins=10)

    plt.title("Science Score Distribution")
    plt.xlabel("Science Score")
    plt.ylabel("Frequency") 

    plt.show() 
    return len(df)

show_science_distribution("labs/lab09/data/students.csv")