# ax^2 + bx + c = 0
import math
_a = float(input('hệ số a='))
_b = float(input('hệ số b='))
_c = float(input('hệ số c='))
print('Phương trình bậc 2 {}x^2+{}x+{}=0 có nghiệm là'.format(_a,_b,_c))
if _a==0:
    if  _b==0 and _c==0:
        print('Phương trình vô số nghiệm')
    elif _b==0 and _c!=0:
        print('Phương trình vô nghiệm')
    else:
        print('x=',_b/_c)
elif _a!=0:
    _delta = _b**2 - 4*_a*_c
    if _delta<0:
        print('Phương trình vô nghiệm')
    elif _delta==0:
        print('Phương trình có nghiệm kép x = ', -_b/2*_a)
    else:
        _x1 = (-_b+math.sqrt(_delta))/2*_a
        _x2 = (-_b-math.sqrt(_delta))/2*_a
        print('Phương tình có 2 nghiệm phân biệt x1 = {} & x2 = {}'.format(_x1,_x2))
        