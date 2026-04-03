import pandas as pd
import matplotlib.pyplot as plt


def show_math_trend(filename):
    df = pd.read_csv("labs/lab09/data/students.csv")

    # Plot Math scores using DataFrame column
    plt.plot(df.index, df['Math'])

    # label bahagian x
    plt.xlabel("Student Index")

    # label bahagian y
    plt.ylabel(" Score")
    plt.title("Math Scores Across Students")

    #utk show graph
    plt.show()