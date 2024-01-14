def is_happy_number(n):
    s = set()
    while n != 1:
        n = sum(int(i)**2 for i in str(n))
        if n in s:
            return False 
        s.add(n)
    return True 

print(is_happy_number(7))
print(is_happy_number(932))
print(is_happy_number(6))
