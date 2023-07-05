import math
a = int(input("Nhap gia tri cua a = "))
b = int(input("Nhap gia tri cua b = "))
for i in range(a,b+1):
        k = int(math.sqrt(i)) + 1
        for j in range(2, k):
            if i % j == 0:
                break
        else:
            print(i)
