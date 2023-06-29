def tinhtong(n):
    if n//10 == 0:
        return n
    return n%10 + tinhtong(n//10)

n = int(input("Nhap n = "))
print("So " + str(n) + " co tong cac chu so la: " + str(tinhtong(n)) )

