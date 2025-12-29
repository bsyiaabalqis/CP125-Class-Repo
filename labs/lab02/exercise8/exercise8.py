def calculate_bounce_height(current_height):
    """
    Calculate the next bounce height (80% of current).
    """
    return current_height * 0.80 


def is_ball_stopped(height):
    """
    Check if the ball has stopped (height < 1).
    """
    return height < 1 
    

def calculate_bounce_count(initial_height):
    """
    Count how many times the ball bounces.
    """
    bounce_count = 0 
    height = initial_height 

    while True: 
        calculate_bounce_height(height)
        if is_ball_stopped(height): 
            break 
        bounce_count +=1 
    return bounce_count 


def calculate_total_distance(initial_height):
    """
    Calculate total distance traveled.
    """
    total_distance = initial_height
    height = initial_height 

    while True:
        height = calculate_bounce_height(height)
        if is_ball_stopped(height): 
            break 
        total_distance += height * 2 
    return total_distance 