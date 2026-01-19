
def find_largest_drop(readings):
    """
    Return the largest consecutive temperature drop, or 0.0 if none.
    """
    max_drop = 0.0
    for i in range(len(readings)-1):
        current_reading = readings[i]
        next_reading = readings[i+1]

        drop = current_reading - next_reading 

        if drop > max_drop:
            max_drop = drop 

    return max_drop 

temps = (32.5, 31.0, 31.5, 28.0, 24.5)
result = find_largest_drop(temps)
print(f"Largest Drop: {result}")  # Expected: 3.5
