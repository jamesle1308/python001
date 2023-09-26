_tensp = input('nhập tên sp: ')
_sl = int(input('số lượng mua: '))
_dongia = int(input('đơn giá: '))
_tongdonhang= _sl*_dongia
if _tongdonhang>130000:
    _tongdonhang*=0.9
else:
    _tongdonhang=_tongdonhang
print('tổng đơn hàng {} là {}'.format(_tensp,_tongdonhang))
