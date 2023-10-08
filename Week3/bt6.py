# Bài 6: Sử dụng lambda tính chu vi và diện tích của hình chữ nhât
_chuvi = lambda a,b: (a+b)*2
_dientich = lambda a,b: a*b
a,b = eval(input("nhập cd, cr của hình chữ nhật"))
print("chu vi hcn",_chuvi(a,b))
print("Diện tích hcn",_dientich(a,b))