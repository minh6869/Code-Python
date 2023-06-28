def giaithua(n):
        gt = 1
        for i in range(2, n+1):
            gt = gt * i
        return gt
a = int(input("Nhập giá trị n: "))
print("N! =", giaithua(a))
