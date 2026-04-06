import pandas as pd


def promotion_candidates(filename):
    df = pd.read_csv(filename) 
    company_avg = df['PerformanceScore'].mean() 

    promotion = df[(df['PerformanceScore']> company_avg) & (df['YearsOfService']>= 2)]

    results = {
        "average_performance": company_avg,
        "min_years_required": 2 ,
        "candidate_count": len(promotion),
        "candidate_names": set(promotion['EmployeeName'])
    }

    return results 

result = promotion_candidates("labs/lab09/data/employees.csv")
print(result)