_sokwtieuthu = int(input("Số KW tiêu thụ = "))
if _sokwtieuthu<50:
    _tiendien = _sokwtieuthu*1678
elif 51<_sokwtieuthu<100:
    _tiendien = int(50*1678 + (_sokwtieuthu-50)*1734)
elif 101<_sokwtieuthu<200:
    _tiendien = int(50*1678 + 50*1734 + (_sokwtieuthu-100)*2014)
elif 201<_sokwtieuthu<300:
    _tiendien = int(50*1678 + 50*1734 + 100*2014 + (_sokwtieuthu-200)*2536)
elif 301<_sokwtieuthu<400:
    _tiendien = int(50*1678 + 50*1734 + 100*2014 + 100*2536 + (_sokwtieuthu-300)*2834)
else:
    _tiendien = int(50*1678 + 50*1734 + 100*2014 + 100*2536 + 100*2834 + (_sokwtieuthu-400)*2927)

print("Số lượng điện tiêu thụ là ",_sokwtieuthu)
print("Số tiền điện phải trả là", _tiendien)