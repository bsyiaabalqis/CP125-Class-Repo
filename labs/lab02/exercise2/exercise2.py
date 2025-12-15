# Lab 02 Exercise 2: Camping Logistics
# Write your code below:

import math

def calculate_event_cost(participants, tent_capacity, tent_price, meal_price):
    # Calculate total_tent 
    total_tent =math.ceil(participants / tent_capacity)

    #Calculate total_tent_price
    total_tent_price = total_tent * tent_price 

    # Calculate total food price
    total_food_price = meal_price * participants 

    # Calculate total cost 
    total_cost =  total_tent_price + total_food_price
    return total_cost 

# Test your code here
print("Testing Camping Logistics...")
