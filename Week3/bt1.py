#Định nghĩa hàm
def _tinhBmi(_height,_weight):
    _bmi = _weight/_height**2
    return _bmi
def _loiKhuyen(_bmi):
    if 0<_bmi<18:
        print("Gầy. cần ăn thêm")
    elif 18<_bmi<25:
        print("Cân đối. Duy trì")
    else:
        print("Mập. cần giảm cân")

#gọi hàm nè
_cao = float(input("Nhập chiều cao của bạn"))
_nang = float(input("Nhập cân năng của bạn"))
_bmiIndex =_tinhBmi(_cao,_nang)
_loiKhuyen(_bmiIndex)