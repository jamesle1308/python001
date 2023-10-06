# Bài 12: Viết chương trình cho phép người dùng nhập vào list số lst_int gồm các phần tử có giá trị tùy ý (nhưng không vượt quá 0-99) - 3 số.
# Máy tính sẽ phát sinh một con số may mắn bất kì: lucky_number trong phạm vi từ  0- 99;
# Nếu lucky_number có trong lst_int thì in ra: "Chúc mừng, bạn đã trúng thưởng!"
# Nếu lucky_number không có trong lst_int thì in ra: "Chúc bạn may mắn lần sau"
import random
_luckyNumber=random.randint(0,100)
_soLuot=3
_lstSo = []
# Viết lại dùng vòng lặp for
# viết lại nếu không phải dữ liệu số thì mất lượt
while _soLuot>0:
    _nhapSo = int(input("Nhập số từ 0-99 ở đây:"))
    if 0<=_nhapSo<=99:
        _lstSo.append(_nhapSo)
    _soLuot-=1
    print("Danh sách các số bạn chọn là",_lstSo)
print("Con số may mắn lần này là",_luckyNumber)
if _luckyNumber in _lstSo:
    print("Chúc mừng bạn trùng 2 tỷ VND")
else:
    print("Thử lại lần nhau nha")
