from functools import reduce
# BUILT IN FUNCTION
# Thường được dùng cho kiểu dữ liệu List là chủ yếu hoặc Set hoặc Dict nhưng phải chỉ định Key hay value (phức tạp)
_lstSo = [-5,10,3,24,54,5,11,19,28,29,9]
_lstDouble = list(map(lambda x:x*2,_lstSo))
print(_lstDouble)

#Đối với filter, chỉ hiểu 1 True 2 False
def _checkPrime(_so):
    if _so<2:
        return False
    elif _so==2:
        return True
    else:
        for i in range (2,_so):
            if _so%i==0:
                return False
            else:
                return True
_lstSNT = list(filter(_checkPrime,_lstSo)) #Hàm filter tự hiểu ko cần truyền biến vào
print(_lstSNT)

_tich = reduce(lambda x,y:x*y,_lstSo)
print(_tich)

