"""
    Determines if a year is a leap year according to the Gregorian calendar.
    
    Rules:
    1. If divisible by 4 -> Yes
    2. BUT if divisible by 100 -> No
    3. UNLESS divisible by 400 -> Yes
    
    Parameters:
    year: Integer year value
    
    Returns:
    True if leap year, False otherwise
    """
    # TODO: Implement the leap year logic
    # Hint: Check divisibility in the correct order
    
def is_leap_year(year): 
    if year % 400 == 0:
        return True 
    elif year % 100 == 0: 
        return False 
    elif year % 4 == 0:
        return True
    else:
       return False

result= is_leap_year(2024)
result= is_leap_year(1900)
result= is_leap_year(2000)