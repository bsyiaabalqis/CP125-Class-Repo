def validate_entry(name, pin):
    if name == "Director" and pin == 1122:
        return True
    elif name == "Security" and pin == 9900:
        return True
    else: 
        return False 

result1 = validate_entry("Director",1122)
result2 = validate_entry("Security", 9900)

# Test your code here
print("Testing Secure Vault System...")
