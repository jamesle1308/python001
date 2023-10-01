_lstSo1 = [5,8,0,-11,9,6,23,15,56,11,90,0,5,23]
# _lstSo2 = _lstSo1 
# Không được gán trực tiếp List như trên vì List sẽ gán vùng nhớ đã được cấp không phải gán giá trị
# Nếu muốn gán thì dùng lệnh copy()
_lstSo2 = _lstSo1.copy()
print("List 1: ",_lstSo1)
print("List 2: ",_lstSo2)
###### Xóa phần tử trong list có 3 cách
# Cách 1 - lệnh pop
# pop có chức năng khá đặc biệt là có thể trả về giá trị của ***PHẦN TỬ*** trong list đã xóa
_soXoa = _lstSo1.pop(3)
print("List sau khi xóa",_lstSo1)
print("Giá trị của phần tử đã xóa",_soXoa)
# Cách 2 - lệnh del
del(_lstSo1[-1])
print("List sau khi xóa",_lstSo1)
print("List 2 (đã copy từ list 1): ",_lstSo2)
# Cách 3 - lệnh remove
_lstSo1.remove(0)
print("List sau khi xóa",_lstSo1)
###### Tìm vị trí của phần tử trong list
_vt=_lstSo1.index(0)
print("Vị trí phần tử muốn tìm",_vt)
###### Thêm phần tử vào list
# Lệnh append thì thêm vào cuối list
# Lệnh insert thì chỉ dịnh được vị trí thêm vào
_lstSo1.insert(9,25)
print("List sau khi thêm",_lstSo1)
###### Cập nhật giá trị phần tử
_lstSo1[2]=31
print("List sau khi thêm",_lstSo1)