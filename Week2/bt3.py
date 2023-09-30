while True:
    _so = int(input('nhập một số cần tính toán: '))
    if _so>0:
        break
    else:
        print("Nhập một số >0 nha bạn")
_tongchan = 0
_tongle = 0
_tich = 1
_tichchiahetcho3 = 1
_strtongchan = "A="
_strtongle = "B="
_strtich = "C="
_strtich2 = "D="
#tính tổng chẵn
for i in range (0,_so+1,2):
    _tongchan += i
    _strtongchan += str(i)+"+"
_strtongchan = _strtongchan.rstrip("+") + "="
#tính tổng lẻ
for i in range (1,_so+1,2):
    _tongle += i
    _strtongle += str(i)+"+"
_strtongle = _strtongle.rstrip("+") + "="
#Tính tích
for i in range (1,_so+1,1):
    _tich *= i
    _strtich += str(i)+"x"
_strtich = _strtich.rstrip("x") + "="
#Tính tích chia hết cho 3
for i in range(1,_so+1,1):
# for i in range (3,_so+1,3)
    if i%3!=0:
        continue
    # if i%3 ==0:
    _tichchiahetcho3 *= i
    _strtich2 += str(i) +"x"
_strtich2 = _strtich2.rstrip("x") + "="

print(_strtongchan,_tongchan)
print(_strtongle,_tongle)
print(_strtich,_tich)
print(_strtich2,_tichchiahetcho3)