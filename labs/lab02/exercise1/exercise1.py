# Lab 02 Exercise 1: Road Trip Budgeter
# Write your code below:


def is_budget_sufficient(one_way_km, km_per_liter, price_per_liter, budget):
    # TODO: Implement this function
    # Calculate round trip cost and checks if within budget
    # Calculate total distance 
    total_distance = one_way_km * 2

    # Calculate liters_used
   liters_used = total_distance/ km_per_liter

    # Calculate 
    


def determine_status(budget):
    if total_cost < budget :
        return "True"
    else: 
        return "False" 
    
result = is_budget_sufficient(10,20,10,500):
# Test your code here
print("Testing Road Trip Budgeter...")
