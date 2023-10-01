_lstSo1 = [5,8,0,-11,9,6,23,15,56,11,90,0,5,23]
_lstSo2 = [7,6,12,645,3258]

# 2 cách extend dữ liệu
# Cách 1 dùng biến trùng gian
_lstSo3 = _lstSo1 + _lstSo2
print("List mở rộng bằng cách 1:",_lstSo3)
# Cách 2 dùng hàm extend
_lstSo1.extend(_lstSo2)
print("List mở rộng bằng cách 2:",_lstSo1)