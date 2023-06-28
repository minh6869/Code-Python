import math
a = 10000000
print("Ban co " + str(a) + " dong")
print("Sau 10 nam ban co " + str( a * 1.051**10) + " dong")
result = int(math.log(50000000 / 10000000, 10) / math.log(1 + 0.051, 10))
print("Sau it nhat " + str(result+1) + " nam ban se co nhieu hon 50 trieu dong")
