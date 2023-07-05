a = int(input("A = "))
b = int(input("B = "))
tmp1 = a
tmp2 = b
boichungmax = 0
while (b > 0):
    if(a > b):
        a,b = b, a % b
    else:
        a,b = a, b % a

boichungmax = tmp1 * tmp2 // a
print("Uoc chung lon nhat la: " + str(a) + " va boi chung nho nhat la: " + str(boichungmax))
