from math import sqrt

def squaresum(target):
    left, right = 0,int(sqrt(target))

    while left <= right:
        current_sum = left ** 2 + right ** 2 

        if current_sum == target:
            return True
        
        elif current_sum < target:
            left += 1
        else:
            right -= 1 

    return False 

print(squaresum(5))