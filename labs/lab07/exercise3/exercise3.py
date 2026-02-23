def compare_prices(store_a, store_b):
    result = {
        "only_a": [],
        "a_cheaper": [],
        "b_cheaper": []
    }

    for item in store_a:
        if item not in store_b:
            result["only_a"].append(item)
        elif store_a[item] < store_b[item]:
            result["a_cheaper"].append(item)
        elif store_b[item] < store_a[item]:
            result["b_cheaper"].append(item)

    result["only_a"].sort()
    result["a_cheaper"].sort()
    result["b_cheaper"].sort()
    
    return result # This MUST be here and indented!
   
store_a = {"milk": 3.50, "bread": 2.00, "eggs": 5.00, "butter": 4.50}
store_b = {"milk": 3.00, "bread": 2.50, "eggs": 5.00, "coffee": 8.00}
result = compare_prices(store_a, store_b)
print(result["only_a"])
print(result["a_cheaper"])
print(result["b_cheaper"])
