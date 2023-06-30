diemtb = float(input("Nhap diem trung binh: "))
print("Xếp loại yếu" if diemtb < 3.5 and diemtb >=0 else 
      "Xếp loại kém" if diemtb < 5 else 
      "Xếp loại trung bình" if diemtb < 6.5 else
      "Xếp loại khá" if diemtb < 8 else
      "Xếp loại giỏi" if diemtb < 9 else
      "Xếp loại xuất sắc" if diemtb <= 10 else
      "Điểm nhập vào không hợp lệ")
