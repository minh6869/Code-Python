def average(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total /len(numbers)
a = int(input("Nhap a = "))
b = int(input("Nhap b = "))
c = int(input("Nhap c = "))
d = int(input("Nhap d = "))
e = int(input("Nhap e = "))
print(average(a,b,c,d,e))
