_lstSo = [5,8,0,-11,9,6,23,15,56,11,90,0,5,23]
print('Tính tổng các phaafntuwr trong List:', sum(_lstSo))
print('Trong list có',len(_lstSo),'phần tử')
print('Trung bình cộng của các phần tử: %.1f'%(sum(_lstSo)/len(_lstSo)))
print('GTLN:',max(_lstSo))
print('GTNL:',min(_lstSo))
# Sắp xếp tăng dần
_lstSo.sort()
print('List tăng dần',_lstSo)
# Sắp xếp giảm dần - cách gián tiếp
_lstSo.reverse()
print('List giảm dần',_lstSo)
# _lstSo.sort(reverse=True) -  đây là cách trực tiếp
