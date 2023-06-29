import math
def area(a,b,c):
    if a+b > c and a+c > b and b+c > a:
        p = (a+b+c)/2
        return "Dien tich cua tam giac co ba canh nhap vao la: " + str(math.sqrt(p*(p-a)*(p-b)*(p-c)))
    else:
        return "Do dai ba canh nhap vao khong tao thanh mot tam giac"

a = int(input("Nhap a = "))
b = int(input("Nhap b = "))
c = int(input("Nhap c = "))
print(area(a,b,c))
