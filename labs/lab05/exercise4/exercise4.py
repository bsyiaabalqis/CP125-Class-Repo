
def filter_query_times(times):
    """
    Remove slow outliers (mean + std deviation) and return sorted times.
    """

    mean = sum(times) / len(times)
    variance = (sum((times[i]-mean)**2))/ len(times)
    std_dev = variance ** 0.5

    outlier = mean + std_dev 

    for i in times:
        if i > outlier:
            i 
       


# Test
query_times = [45, 52, 48, 180, 51, 47, 50, 12]
result = filter_query_times(query_times)
print(f"Filtered Times: {result}")  
# Expected: [12, 45, 47, 48, 50, 51, 52]
