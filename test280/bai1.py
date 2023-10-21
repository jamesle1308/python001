while True:
    _so1, _so2 = eval(input("Nhập 2 số để kiểm tra: "))
    assert(_so1>0 and _so2>0), "Số nhập vào phải >0"
    break
_tonguocSo1=0
_tonguocSo2=0
print("Các ước Số 1: ")
for i in range(1,_so1):
    if _so1%i ==0:
        _tonguocSo1 +=i
        print(i, end=",")
print("\n")
print("Các ước Số 2: ")
for i in range(1,_so2):
    if _so2%i ==0:
        _tonguocSo2 +=i
        print(i, end=",")
print("\n")
print(_tonguocSo1)
print(_tonguocSo2)
if (_tonguocSo1-_so2) == 1 or (_tonguocSo2-_so1) == 1:
    print("2 số này là 2 số hứa hôn")
else:
    print("Số này fail rồi")