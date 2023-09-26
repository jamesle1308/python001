# Bài tập về nhà 20,21,22

_loaixe=int(input('loại xe: '))
_thoigiancho=int(input('Thời gian chờ (Phút): '))
_tiendichuyen = 0
_sokmdichuyen=int(input('Số km di chuyển: '))
if _thoigiancho<=5:
    _tiencho = 0
else:    
    _tiencho = (_thoigiancho-5)*750

if _loaixe==4:
    if _sokmdichuyen<0.5:
        _tiendichuyen = _sokmdichuyen*11000
    elif 0.5<_sokmdichuyen<30:
        _tiendichuyen = int(0.5*11000 + (_sokmdichuyen-0.5)*17600)
    else:
        _tiendichuyen = int(0.5*11000 + (29.5)*17600 + (_sokmdichuyen-30)*14500)
else: 
    if _sokmdichuyen<0.5:
        _tiendichuyen = _sokmdichuyen*12000
    elif 0.5<_sokmdichuyen<30:
        _tiendichuyen = int(0.5*12000 + (_sokmdichuyen-0.5)*19600)
    else:
        _tiendichuyen = int(0.5*12000 + (29.5)*19600 + (_sokmdichuyen-30)*17100)

_tiencuoc = _tiendichuyen + _tiencho

print(_loaixe)
print(_sokmdichuyen)
print(_tiencho)
print(_tiendichuyen)
print(_tiencuoc)