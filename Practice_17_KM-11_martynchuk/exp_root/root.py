import math
def root2(a):
    if a < 0:
        raise ValueError("Число повинно бути додатним для кореня")
    return math.sqrt(a)

def root3(b):
    return b ** (1 / 3)



