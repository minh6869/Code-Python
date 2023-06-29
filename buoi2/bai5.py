def check(n):
    a=0
    b=1
    F = a+b
    while F < n:
        a=b
        b=F
        F = a+b
    return F
n = int(input("Nhap n = "))
if check(n) == n or n == 0:
    print("So " + str(n) + " la so fibonacii")
else:
    print("So " + str(n) + " khong la so fibonacii")

