# Lab 02 Exercise 4: Dynamic Parking Rate
# Write your code below:

def get_hourly_rate(vehicle_type, hour_24):
    if vehicle_type == "Electric":
        return 2.0 
    elif vehicle_type == "Hybrid":
        if hour_24 >= 22 or hour_24 <= 6:
            return 2.00 
        else: 
            return 5.00
    else:
        return 5.00 
    
print (get_hourly_rate("Electric",3))
print (get_hourly_rate("Hybrid",5))
print (get_hourly_rate("Hybrid",22))

    # TODO: Implement this function
    # Return hourly rate based on vehicle and time
   

# Test your code here
print("Testing Dynamic Parking Rate...")
