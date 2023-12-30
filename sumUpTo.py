def sumUpTo(number):
    if number <= 1:
        return 1
    
    return number + sumUpTo(number - 1)

print(sumUpTo(12)) # 78