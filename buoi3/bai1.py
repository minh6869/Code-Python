import math

def isprime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

n = int(input("Nhập giá trị của n = "))
if isprime(n):
    print(str(n) + " là số nguyên tố")
else:
    print(str(n) + " không là số nguyên tố")
