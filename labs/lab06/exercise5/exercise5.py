def audit_zero_trust(baseline_set, current_log_list):
    log_set = set(current_log_list)
    authorized = baseline_set.intersection(log_set)
    alert = log_set.difference(baseline_set)
    inactive = baseline_set.difference(current_log_list)

    return authorized, alert, inactive 

baseline_set = {( "u1", "192.168.1.1" ), ( "u2", "192.168.1.5" )}
current_log_list = [( "u1", "192.168.1.1" ), ( "u3", "10.0.0.99" )]