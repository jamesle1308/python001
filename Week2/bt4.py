# x=float(input("Nhập vào x = "))
# y=float(input("Nhập vào y = "))
_ketqua = 0
while True:
    x,y = eval(input("Nhập 2 số x và y theo thứ tự là "))
    if y>x:
        for i in range(x,y+1,1):
            _ketqua += i*i 
            # _ketqua += i**2
            print(_ketqua)
        break #break này thuộc về WHILE IF trên nên thụt dòng bằng FOR
    else:
        print("vui lòng nhập một số y>x & kết quả =",_ketqua)
