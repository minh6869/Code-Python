a = int(input("Nhap a = "))
b = int(input("Nhap b = "))
c = int(input("Nhap c = "))
print(str(a) if a > b and a > c or b == c else
      str(b) if b > a and b > c or a == c else
      str(c) if c > a and c > b or a == b else
      "3 số có giá trị bằng nhau")
