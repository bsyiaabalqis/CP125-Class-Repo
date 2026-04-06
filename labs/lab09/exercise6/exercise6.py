import pandas as pd


def critical_inventory(filename):
    df = pd.read_csv(filename) 

    critical = df[df['StockLevel'] < df['ReorderThreshold']]
    result ={ 
        "total_products" : len(df),
        "critical_count": len(critical),
     "critical_products": set(critical['ProductName'])
    }
    return result

result = critical_inventory("labs/lab09/data/inventory.csv")
print(result)