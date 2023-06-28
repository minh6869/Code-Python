x = int(input("Nhap so nguyen x = "))
dem=0
tmp1 = x
while x!=0:
    dem+=1
    x//=10
    if(x<10 and x > 0):
        tmp2 = x
print("So " + str(tmp1) + " co "+ str(dem) + " chu so")
print("Chu so dau tien la:", tmp2)
