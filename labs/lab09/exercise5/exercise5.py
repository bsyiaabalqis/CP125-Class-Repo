import pandas as pd


def high_performers(filename):
    df = pd.read_csv(filename) 

    #filter rows
    excellent = df[(df['Math']> 85) & (df['Science']> 85) & (df['English']> 85) & (df['Physics']> 85) & (df['Chemistry']> 85) ]
    
    result = {
        "count": len(excellent),  #check brpa count utk students yg excellent
        "names" : set(excellent['Name']) #listkn smua nama excellent based on the syarat atas
    }

    return result 

result = high_performers("labs/lab09/data/students.csv")
print(result)
