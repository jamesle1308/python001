#  Bài 5:
# Viết chương trình in ra màn hình tam giác Pascal theo định dạng.
import math
def _tinhC (k,n):
    _c = int(math.factorial(n)/(math.factorial(k)*math.factorial(n-k)))
    return _c
n = int(input("Nhập số dương mong muón"))
for i in range(0, n+1):
    for j in range(0, i+1):
        _c=_tinhC(j,i)
        print(_c,end="\t")
    print("\n")