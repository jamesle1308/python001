# ax + b = 0
_a = float(input('hệ số a='))
_b = float(input('hệ số b='))
_x= -_b/_a
print('Phương trình bậc 1 {}x+{}=0 có nghiệm là'.format(_a,_b))
if  _a==0 and _b==0:
    print('Phương trình vô số nghiệm')
elif _a==0 and _b!=0:
    print('Phương trình vô nghiệm')
else:
    print('x=',_x)

