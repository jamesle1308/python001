_so1=float(input('nhập số thứ 1:'))
_so2=float(input('nhập số thứ 2:'))
_tong=_so1+_so2
_hieu=_so1-_so2
_tich=_so1*_so2
_thuong=_so1/_so2
#cách 1 - dùng dấy phẩy
print("Tổng =",_tong, "Hiệu",_hieu, "Tích",_tich, "Thương",_thuong)
#cách 2 - dùng % lấy số thập phân dùng thay thế
print("Thương= %.2f"%(_so1/_so2))
#cách 3 - dùng .format
######Dùng dấu {} bao nhiều lần thì .format phải có bấy nhiêu giá trị
print("{:.3f}:{:.3f}={:.2f}".format(_so1,_so2,_so1/_so2))

