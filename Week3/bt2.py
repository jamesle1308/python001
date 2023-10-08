# Bài 2: Viết chương trình nhập vào 2 số a và b, kiểm tra xem 2 số đó có phải là 2 số thân thiết hay không?  
# (biết 2 số nguyên dương a và b  được gọi là 2 số thân thiết khi và chỉ khi tổng các ước của số a (không kể chính nó) bằng số b và ngược lại).
# Bộ ktr 220 & 284
def _timUoc (_so):
    _lstUoc = []
    for i in range (1,_so):
        if _so%i ==0:
            _lstUoc.append(i)
    return _lstUoc

while True:
    _a, _b = eval(input("Nhập 2 số a,b để ktr"))
    if _a>0 and _b>0:
        break
    else:
        print("Vui lòng nhập 2 số lớn hơn 0")

_lstUoc1 = _timUoc(_a)
_lstUoc2 = _timUoc(_b)
if sum(_lstUoc1)==_b and sum(_lstUoc2)==_a :
    print ("2 số a,b là 2 số thân thiết")
else:
    print ("2 số a,b ko phải là số thân thiết")

