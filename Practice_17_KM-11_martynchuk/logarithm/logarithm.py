import math
def log(base, num):
    if base <= 0 or base == 1 or num <= 0:
        raise ValueError("Неправильні значення основи або числа")
    return math.log(num, base)

def ln(num):
    if num <= 0:
        raise ValueError("Число повинно бути додатним для логарифма")
    return math.log(num)

def lg(num):
    if num <= 0:
        raise ValueError("Число повинно бути додатним для логарифма")
    return math.log10(num)