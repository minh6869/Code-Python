import math
def area2(xa,ya,xb,yb,xc,yc):
    AB = math.sqrt( (xb - xa)**2 + (yb-ya)**2)
    AC = math.sqrt( (xc - xa)**2 + (yc-ya)**2)
    BC = math.sqrt( (xc - xb)**2 + (yb-yc)**2)
    p = (AB + AC + BC)/2
    S = round(math.sqrt( p*(p-AB)*(p-AC)*(p-BC) ), 6)
    if AB + AC > BC and AB + BC > AC and BC + AC > AB:
        return "Dien tich tam giac ma ba diem tao thanh la: " + str(S)
    else:
        return "Toa do ba diem da nhap khong tao thanh mot tam giac"

xa = int(input("Nhap xa: "))
ya = int(input("Nhap ya: "))
xb = int(input("Nhap xb: "))
yb = int(input("Nhap yb: "))
xc = int(input("Nhap xc: "))
yc = int(input("Nhap yc: "))
print(area2(xa,ya,xb,yb,xc,yc))
