import math

def isprime(A, B):
    for num in range( max(min(A, B), 2), max(A, B)):
        is_prime = True
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num)

A = int(input("Nhap gia tri cua A: "))
B = int(input("Nhap gia tri cua B: "))
isprime(A, B)
