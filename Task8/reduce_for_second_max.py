from functools import reduce

def find_second_max(current: tuple[int, int], next_value: int) -> tuple[int, int]:
    first_max, second_max = current
    
    if first_max is None:
        return (next_value, second_max)
    
    if next_value >= first_max:
        return (next_value, first_max)
        
    if second_max is None or next_value > second_max:
       return (first_max, next_value)
        
    return current
    

max_value, second_max = reduce(find_second_max, [7, 1, 2, 3, 4, 5], (None, None))        
        
print(second_max) # 5
