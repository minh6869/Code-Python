x = int(input("Nhap so nguyen khong am: "))
if x < 0:
    print("Vi ban da nhap so am nen chuong trinh se dung lai\nBye!")
else:
    print("Nhap tiep cho den khi nhap so am thi chuong trinh se dung lai")
    while x >= 0:
        x = int(input())
        if x < 0:
            print("Vi ban da nhap so am nen chuong trinh se dung lai\nBye!")

