
def analyze_performance(lap_times):
    mid = len(lap_times) // 2

    if len(lap_times) % 2 == 1: 
        mid += 1
    
    

total = sum (laps)
count = len(laps)
average = total / count
laps = [60, 62, 61, 63, 65, 68, 70, 72]
result = analyze_performance(laps)
print(f"Faded: {result}")  # Expected: True
