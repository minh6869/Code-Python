def checknam(n):
    if n % 4 == 0 and n % 100 != 0 or n % 400 == 0:
        return 1
    return 0
ngay = int(input("Nhap ngay: "))
thang = int(input("Nhap thang: "))
nam = int(input("Nhap nam: "))
dem=0
if 1 <= ngay and ngay <= 27 and 1 <= thang and thang <= 12:
    ngay+=1
elif ngay == 28 and thang == 2:
    if checknam(nam) == 1:
        ngay+=1
    else:
        ngay = 1
        thang += 1
elif ngay == 29 and thang == 2:
    if checknam(nam) == 1:
        ngay=1
        thang+=1
    else:
        dem+=1
        #print("Ngay thang khong hop le")
elif ngay == 31:
    if thang in [1,3,5,7,8,10]:
        ngay=1
        thang+=1
    elif thang == 12:
        ngay = 1
        thang = 1
        nam += 1
    else:
        dem+=1
        #print("Ngay thang khong hop le")
elif ngay == 30 and thang != 2:
    if thang in [4, 6, 9, 11]:
        ngay=1
        thang+=1
    else:
        ngay+=1
else:
    dem+=1
    #print("Ngay thang khong hop le")

if dem == 0:
    print("Ngay tiep theo la ngay: " + str(ngay) + "/" + str(thang) + "/" + str(nam))
else:
    print("Ngay thang khong hop le")

        
