def lcm_calculate(a, b):
    least = min(a, b)
    most = max(a,b)
    
    i = 0
    while True:
        factor = least + i
        if(factor % most == 0):
            return factor
        i += least
        
result = lcm_calculate(6,8)

print(result)