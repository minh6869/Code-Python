def uoc_so_chung_lon_nhat(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def boi_so_chung_nho_nhat(a, b):
    return (a * b) // uoc_so_chung_lon_nhat(a, b)

def tim_uoc_boi_chung():
    numbers = []
    while True:
        num = int(input("Nhập số: "))
        if num <= 0:
            print("Kết thúc nhập!")
            break
        numbers.append(num)
    if len(numbers) != 0:
        uscln = numbers[0]
        bscnn = numbers[0]
        for i in range(1, len(numbers)):
            uscln = uoc_so_chung_lon_nhat(uscln, numbers[i])
            bscnn = boi_so_chung_nho_nhat(bscnn, numbers[i])
        print("Dãy đã nhập là: " + str(numbers))
        print("Ước số chung lớn nhất:", uscln)
        print("Bội số chung nhỏ nhất:", bscnn)
    else:
        print("Dãy đã nhập không hợp lệ")

tim_uoc_boi_chung()
