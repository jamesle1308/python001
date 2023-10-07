# Bài 17: Viết chương trình từ điển với các chức năng sau:
# 1. Người dùng chọn chức năng 1: xem từ điển (in ra 2 cột gồm từ Anh và nghĩa Việt)
# 2. Người dùng chọn chức năng 2: cập nhật lại nghĩa tiếng Việt (thông qua từ tiếng Anh)
# 3. Người dùng chọn chức năng 3: thêm từ vào từ điển (kiểm tra xem từ này đã tồn tại chưa, nếu tồn tại rồi thì yêu cầu nhập lại 1 từ khác). Lưu ý: một từ có thể có nhiều nghĩa và lưu nghĩa của từ vào list.
# 4. Người dùng chọn chức năng 4: xóa từ ra khỏi từ điển (thông qua từ tiếng Anh, nếu từ không có trong từ điển thì thông báo tên không tồn tại);
# 5. Nếu người dùng chọn các chức năng khác 4 chức năng trên thì thông báo tác vu sai và thoát khỏi chương trình.
tu_dien={'one':['số 1','con số 1'],'father':['cha','bố']}
while True:
    print("1: xem từ điển")
    print("2: cập nhật lại nghĩa tiếng Việt (thông qua từ tiếng Anh)")
    print("3: thêm từ vào từ điển")
    print("4: xóa từ ra khỏi từ điển (thông qua từ tiếng Anh)")
    _tacvu=input("Nhập tác vụ muốn thực hiện")
    if _tacvu =="1":
        print("{:15}{:30}".format("Từ TA","Nghĩa"))
        for k,v in tu_dien.items():
            print("{:15}{:30}".format(k,",".join(v)))
            # sử dụng function join dùng để tach phần tử trong List thành str - key ở đây là str
            # print("{:15}{:30}".format(k,str(v))) 
            # ép kiểu string cho list - key ở đây là str
    elif _tacvu =="2":
        # pass
        _tuTiengAnh = input("Nhập từ tiếng anh cần sửa nghĩa")
        if _tuTiengAnh in tu_dien:
            _nghiaCu = tu_dien[_tuTiengAnh] # đây đang kiểu List
            _nghiaMoi = input("nhập nghĩa mới cần thêm vào và được cách nhau bởi dấu phẩy") # đây đảng kiểu string
            _lstNghiamoi = _nghiaMoi.split(",") # dùng function split để tách string thành list
            # print(_nghiaCu)
            # print(_nghiaMoi)
            # print(_lstNghiamoi)
            _nghiaCu.extend(_lstNghiamoi)
            tu_dien[_tuTiengAnh] = _nghiaCu
            print("Thêm thành công")
    elif _tacvu =="3":
        # pass
        _tuTiengAnh = input("Nhập từ tiếng anh cần sửa nghĩa")
        if _tuTiengAnh not in tu_dien:
            _nghia=input("Nhập các nghĩa khác nhau bởi dấu phẫy")
            
        else:
            print("Từ tiếng Anh này đã tồn tại, vui lòng cập nhật lại bằng tác vụ 2")
    elif _tacvu =="4":
        # pass
        _tuTiengAnh = input("Nhập từ tiếng anh cần xóa")
        if _tuTiengAnh in tu_dien:
            del(tu_dien[_tuTiengAnh])
            print("Xóa thành công")
        else:
            print("Không tồn tại trong từ điển")
    else:
        print("Dừng chương trình")
        break   