def apply_upgrade(current, upgrade):
    # TODO: Your code here
    result = {
        "current": current.copy(),
        "upgrade": upgrade.copy()
    }

    for key in upgrade:
        if key in current < upgrade[key]: 
            result = upgrade[key]
    pass



current = {"read": 2, "write": 1, "admin": 0}
upgrade = {"read": 1, "write": 3, "execute": 2}
result = apply_upgrade(current, upgrade)
print(result)
print(current)   # Should be unchanged
