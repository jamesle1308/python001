_listNhap=[]
while True:
    _so=int(input("Nhập một số đưa vào danh sách: "))
    _listNhap.append(_so)
    _luachon=input("Nhập y hoặc Y để bổ sung danh sách: ")
    if _luachon != "y" and _luachon != "Y":
        break
print("List vừa nhập là: ",_listNhap)