# 1. SỐ EMIRP(2 điểm)
# Yêu cầu : Nhập vào một số nguyên dương n, kiểm tra số đó có phải là số EMIRP hay
# không, biết số EMIRP là một số mà chính bản thân nó và số đối xứng của nó đều là số
# nguyên tố.

a = int(input("Nhập vào 1 số nguyên dương: "))

while True:
    if a > 0:
        break
    else: 
        print("Vui lòng nhập vào một số nguyên dương >0")

_so = str(a)
_sodoi = _so[::-1]
_intso = int(_so)
_intsodoi = int(_sodoi)
# print(type(_so))
# print(type(_sodoi))
# print(type(_intso))
# print(type(_intsodoi))

if _so==2:
    print("2 là số nguyên tố")
else:
    for i in range(2,_intso):
        if _intso%i==0:
            # print(_so,"Ko phải số nguyên tố")
            break
    else:
        _lableso = 1
        # print(_so,"Là số nguyên tố")
    
    for i in range(2,int(_intsodoi)):
        if _intsodoi%i==0:
            break
    else:
        _lablesodoi = 1
        # print(_sodoi,"Là số nguyên tố")

if _lableso == 1 and _lablesodoi == 1:
    print("nhập 1 số để kiểm tra: ",_so)
    print("Số đối xứng: ", _sodoi)
    print(_so, "là số EMIRP")
else:
    print(_so, "không phải số EMIRP")
