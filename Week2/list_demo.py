#list không phải kiểu dữ liệu tính toán. Không dùng các phép toán +=, -= ... cho cấu trúc dữ liệu List mà dùng các lệnh thay thế.
#Tạo các tệp List chẵn và lẽ từ 0-23
_listChan = []
_listLe = []
for i in range(0,21,2):
    _listChan.append(i)
print(_listChan)

for i in range(1,21,2):
    _listLe.append(i)
print(_listLe)