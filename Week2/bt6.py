_so1 = int(input("Nhập số 1: "))
_so2 = int(input("Nhập số 2: "))
while True:
    if _so1>0 and _so2>0:
        break
    else:
        print("xin vui lòng nhập 2 số >0")
_temp1=_so1
_temp2=_so2
while _temp1!=_temp2:
    if _temp1>_temp2:
        _temp1 -= _temp2
    else:
        _temp2 -= _temp1
print("UCLN của {} và {} là {}".format(_so1,_so2,_temp1))


