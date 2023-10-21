import math
while True:
    _so1,_so2=eval(input("Nhập phạm vi số để kiểm tra: "))
    if _so1>1 and _so2>1:
        break
# if _so==2:
#     print("2 là số nguyên tố")
_lst = []
for i in range(_so1,_so2):
    for j in range (2,i):
        if i%j:
            # print(i," không phải là số nguyên tố")
            break
        else:
            _lst.append(i)
print(_lst)