from aifc import _aifc_params


_loaiphong = int(input("Loại phòng là "))
_sodem = int(input("Số đêm ở lại "))
_sotien = 0
if _loaiphong == 1:
    if _sodem == 1:
        _sotien = 1260000
    elif 1<_sodem<4:
        _sotien = 1260000*0.75*_sodem
    else:
        _sotien = 1260000*0.70*_sodem
elif _loaiphong ==2:
    if _sodem == 1:
        _sotien = 1550000
    elif 1<_sodem<4:
        _sotien = 1550000*0.75*_sodem
    else:
        _sotien = 1550000*0.70*_sodem
elif _loaiphong ==3:
    if _sodem == 1:
        _sotien = 1830000
    elif 1<_sodem<4:
        _sotien = 1830000*0.75*_sodem
    else:
        _sotien = 1830000*0.70*_sodem
elif _loaiphong ==4:
    if _sodem == 1:
        _sotien = 1830000
    elif 1<_sodem<4:
        _sotien = 1830000*0.75*_sodem
    else:
        _sotien = 1830000*0.70*_sodem
elif _loaiphong ==5:
    if _sodem == 1:
        _sotien = 2120000
    elif 1<_sodem<4:
        _sotien = 2120000*0.75*_sodem
    else:
        _sotien = 2120000*0.70*_sodem
elif _loaiphong ==6:
    if _sodem == 1:
        _sotien = 2120000
    elif 1<_sodem<4:
        _sotien = 2120000*0.75*_sodem
    else:
        _sotien = 2120000*0.70*_sodem
elif _loaiphong ==7:
    if _sodem == 1:
        _sotien = 2540000
    elif 1<_sodem<4:
        _sotien = 2540000*0.75*_sodem
    else:
        _sotien = 2540000*0.70*_sodem
else:
    if _sodem == 1:
        _sotien = 4800000
    elif 1<_sodem<4:
        _sotien = 4800000*0.75*_sodem
    else:
        _sotien = 4800000*0.70*_sodem

print("Loại phòng là {}, số đêm ở lại là {}".format(_loaiphong,_sodem))
print("Số tiền phải trả là ",_sotien)