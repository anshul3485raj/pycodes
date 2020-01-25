# GCD and LCM are not in math module.  They are in gmpy, but these are simple enough:

def gcd(a,b):
    """Compute the greatest common divisor of a and b"""
    while b > 0:
        a, b = b, a % b
    return a
    
def lcm(a, b):
    """Compute the lowest common multiple of a and b"""
    return a * b / gcd(a, b)

a = 10 
b = 5

while True:
    print(gcd(a, b))
    print(lcm(a, b))
    break
