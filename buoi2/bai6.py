def giaithua(n):
    if n==1:
        return 1
    return n*giaithua(n-1)

n = int(input("Nhap n = "))
tong=0
for i in range(1,n+1):
    tong+=giaithua(i)
print(tong)
