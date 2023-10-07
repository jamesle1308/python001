# Bài 16: Viết chương trình quản lý danh bạ điện thoại như sau:
# 1. Người dùng chọn chức năng 1: xem danh bạ điện thoại (in ra 2 cột gồm sđt và tên)
# 2. Người dùng chọn chức năng 2: cập nhật lại tên thông qua số điện thoại
# 3. Người dùng chọn chức năng 3: thêm mới số điện thoại vào danh bạ
# 4. Người dùng chọn chức năng 4: xóa liên hệ ra khỏi danh bạ 
# 5. Người dùng tìm kiếm số điện thoại thông qua tên
# 6. Nếu người dùng chọn các chức năng khác 4 chức năng trên thì thông báo tác vu sai và thoát khỏi chương trình.
# Dữ liệu khởi tạo: danh_ba={ '0989741258':'Johnny','0903852147':'Katherine','0903712712':'Johnny'}
danh_ba={ '0989741258':'Johnny','0903852147':'Katherine','0903712712':'Johnny'}
print(danh_ba)
print(type(danh_ba))
print(danh_ba.items())
print(type(danh_ba.items()))
while True:
    print("1: xem danh bạ điện thoại")
    print("2: cập nhật lại tên thông qua số điện thoại")
    print("3: thêm mới số điện thoại vào danh bạ")
    print("4: xóa liên hệ ra khỏi danh bạ ")
    print("5: Tìm kiếm số diện thoại")
    _tacvu=input("Nhập tác vụ muốn thực hiện")
    if _tacvu=="1":
        print("{:15}{:15}".format("SĐT","Tên"))
        for k,v in danh_ba.items():
            print("{:15}{:15}".format(k,v))
    elif _tacvu=="2":
        sdt=input("Nhập số điện thoại cần tìm")
        if sdt in danh_ba:
            #kiểu dữ liệu dict sẽ tự hiểu biến sdt là key - quy định là vậy
            ten=input("Nhập tên sẽ cập nhật")
            danh_ba[sdt]=ten
        else:
            print("Số điện thoại không tồn tại")
    elif _tacvu=="3":
        # pass
        sdt=input("Nhập số điện thoại cần thêm")
        if sdt not in danh_ba:
            #kiểu dữ liệu sẽ mặc định thêm vào cuối dictionary nếu ko tồn tại
            ten=input("Nhập tên")
            danh_ba[sdt]=ten
        else:
            print("Số điện thoại đã tồn tại, vui lòng cập nhật thông tin bằng tác vụ 2")
    elif _tacvu=="4":
        # pass
        sdt=input("Nhập số điện thoại cần tìm")
        if sdt in danh_ba:
            del(danh_ba[sdt])
            print("Xóa thành công")
        else:
            print("Số điện thoại không tồn tại trong danh bạ")
    elif _tacvu=="5":
        ten=input("Nhập tên cần tìm")
        _ketqua={}
        for k,v in danh_ba.items():
            if ten.upper()==v.upper():
                _ketqua[k]=v
        if len(_ketqua)>0:
            print("{:15}{:15}".format("SĐT","Tên"))
            for k,v in _ketqua.items():
                print("{:15}{:15}".format(k,v))
        else:
            print("Không có trong danh bạ")
    else:
        print("Dừng chương trình")
        break