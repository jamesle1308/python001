_sotienchovao = int(input('Money: '))
_500ngan = _sotienchovao//500000
# _sotienchovao=_sotienchovao%500000
_sotienchovao%=500000
_400ngan = _sotienchovao//400000
_sotienchovao%=400000
_300ngan = _sotienchovao//300000
_sotienchovao%=300000
_200ngan = _sotienchovao//200000
_sotienchovao%=200000
_100ngan = _sotienchovao//100000
_sotienchovao%=100000
_50ngan = _sotienchovao//50000
_sotienchovao%=50000
print('500.000: %f tờ'%(_500ngan))
print('400.000: %f tờ'%(_400ngan))
print('300.000: %f tờ'%(_300ngan))
print('200.000: %f tờ'%(_200ngan))
print('100.000: %f tờ'%(_100ngan))
print('50.000: %f tờ'%(_50ngan))
print('số tiền còn dư: %f VND'%(_sotienchovao))

# % là phép chia lấy phần dư
# // là phép chcia lấy cận dưới (chỉ lấy số nguyên)