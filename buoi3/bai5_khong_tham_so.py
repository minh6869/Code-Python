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
            break
        numbers.append(num)

    uscln = numbers[0]
    bscnn = numbers[0]
    for i in range(1, len(numbers)):
        uscln = uoc_so_chung_lon_nhat(uscln, numbers[i])
        bscnn = boi_so_chung_nho_nhat(bscnn, numbers[i])

    print("Ước số chung lớn nhất:", uscln)
    print("Bội số chung nhỏ nhất:", bscnn)

tim_uoc_boi_chung()
