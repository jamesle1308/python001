_name= "Lê Huỳnh tú"
# In ra tất cả các kí tự cho tới khi gặp khoảng trắng
for _char in _name:
    if _char ==" ":
        break
    print(_char, end="-")
print("/n")
# in ra tất cả kí tư trừ khoảng trắng
for _char in _name:
    if _char ==" ":
        continue
    print(_char, end="-")
print("/n")
# Lệnh Else có thể kết hợp với vòng lặp For và While &&& chỉ được thực hiện thi break và continue ko thực hiện chức năng của nó. Tức là vòng lặp phải đi hết chuỗi danh sách đó
# Kiểm tra xem trong tập hợp _name có chữ u hay không
for _char in _name:
    if _char =="u":
        break
    print("Chuỗi tên có kí tự u")
else:
    print("Chuỗi name không có kí tự u")