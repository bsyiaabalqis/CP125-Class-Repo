
def is_critical_hit(luck):
    """
    Returns True if luck is above 70.
    """
    if luck > 70:
        return True 
    else:
        return False

def calculate_raw_damage(base_attack, is_crit):
    """
    Doubles the base attack if it's a critical hit.
    """
    if is_crit:
        return base_attack * 2
    return base_attack 

def calculate_final_health(current_health, raw_damage, defense):
    """
    Calculates final health after damage.
    Actual damage = raw_damage - defense.
    Damage cannot be negative.
    Final health cannot go below 0.
    """
    damage = raw_damage - defense 
    if damage < 0: 
        damage = 0

    final_health = current_health - damage 
    if final_health < 0: 
        final_health = 0
    return final_health 