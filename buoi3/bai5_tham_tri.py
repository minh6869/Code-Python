uocmax = 0
boimin = 0

def uoc_chung_max(a,b):
    while b!=0:
        a, b = b, a % b
    return a

def boi_chung_min(a,b):
    return a*b // uoc_chung_max(a,b)

numbers = []
def Nhap_va_tim(uocmax, boimin):
    while 1:
        num = int(input("Nhập số: "))
        if num <= 0:
            print("Kết thúc nhập!")
            break
        numbers.append(num) # Neu so da nhap vao > 0 thi them so do vao cuoi mang numbers
        uocmax = numbers[0]
        boimin = numbers[0]
        for i in range(1, len(numbers)):
            uocmax = uoc_chung_max(uocmax, numbers[i])
            boimin = boi_chung_min(boimin, numbers[i])
    
    return uocmax, boimin

uocmax, boimin = Nhap_va_tim(uocmax, boimin)
if uocmax != 0:
    print("Dãy đã nhập là: ", numbers)
    print("Ước chung lớn nhất của dãy đã nhập là: " + str(uocmax))
    print("Bội chung nhỏ nhất của dãy đã nhập là: " + str(boimin))
else:
    print("Dãy đã nhập không hợp lệ!")


#Đầu tiên khởi tạo 2 biến uocmax và boimin đều bằng 0 hoặc bất kì số nào cũng được.
#Sau đó truyền tham số tham trị của hai biến này vào hàm Nhap_va_tim.
#Tham số tham trị có nghĩa là giá trị của hai biến này sẽ được sao chép vào hai biến mới trong hàm, do đó mọi phép toán nào được thực hiện trên hai biến tronghàm đều không làm thay đổi giá trị của hai biến ban đầu bên ngoài hàm
#Sau khi tính toán trong hàm Nhap_va_tim thì trả lại kết quả cần tìm của bài toán và gán lại cho hai biến uocmax và boimin, sau đó print


