def uoc_chung_max(a,b):
    while b!=0:
        a, b = b, a%b
    return a

def boi_chung_min(a,b):
    return a*b // uoc_chung_max(a,b)

numbers = []
def Nhap_va_tim(uocmax, boimin):
    while 1:
        number = int(input("Nhập số: "))
        if number <=0:
            print("Kết thúc nhập!")
            break
        numbers.append(number) # neu number > 0 thi them so number vao cuoi danh sach numbers
        uocmax[0] = numbers[0]
        boimin[0] = numbers[0]
        for i in range(1, len(numbers)):
            uocmax[0] = uoc_chung_max(uocmax[0], numbers[i])
            boimin[0] = boi_chung_min(boimin[0], numbers[i])

uocmax = [0]
boimin = [0]
Nhap_va_tim(uocmax, boimin)
if uocmax[0] != 0:
    print("Dãy đã nhập là: ",numbers)
    print("Ước chung lớn nhất của dãy vừa nhập là: " + str(uocmax[0]) )
    print("Bội chung nhỏ nhất của dãy vừa nhập là: " + str(boimin[0]) )
else:
    print("Dãy đã nhập không hợp lệ!")

#Trong bài này sử dụng kiểu tham số tham chiếu
#Để truyền tham số tham chiếu của 2 biến uocmax và boimin vào trong hàm Nhap_va_tim, có thể sử dụng kiểu dữ liệu list để đóng gói giá trị hai biến
#Sau đó truyền list này vào hàm 
#Các thay đổi thực hiện trên list trong hàm sẽ ảnh hưởng trực tiếp đến giá trị của hai biến ban đầu 

#Trong đoạn code trên, biến uocmax và boimin được khai báo là list và truyền vào hàm Nhap_va_tim dưới dạng list
#Bên trong hàm, giá trị của hai biến được gán vào uocmax[0] và boimin[0] 
#Các thay đổi trên uocmax[0] và boimin[0] sẽ thay đổi trực tiếp đến giá trị của uocmax và boimin bên ngoài hàm vì thế mới gọi là tham chiếu:)

        
