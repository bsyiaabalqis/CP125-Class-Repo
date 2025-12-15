def is_valid_triangle(a,b,c):
    if a <= 0 and b <= 0 and c <= 0: 
         return False 
    
    if (a + b > c) and (a + c > b) and (b + c > a):
        return True
    else: 
        return False 
    
result = is_valid_triangle(1,3,8)