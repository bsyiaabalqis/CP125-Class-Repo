import pandas as pd
import matplotlib.pyplot as plt

def explore_data(filename):
    # loads csv into dataframe
    df = pd.read_csv(filename) 

    # calculate required statistics
    total_students = len(df)
    subjects = list(df.columns[1:])
