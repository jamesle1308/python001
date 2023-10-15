from libs.functions import *
_path = "files/quanlykho.csv"
while True:
    print("Phần mềm quản lý kho")
    print("1: Xem danh sách các mặt hàng lưu trong file")
    print("2: Thêm các mặt hàng mới (mã mặt hàng không trùng nhau)")
    print("3: Cập nhật lại thông tin mặt hàng (thông qua mã)")
    print("4: Xóa mặt hàng ra khỏi file (thông qua mã)")
    print("5: Lọc ra mặt hàng có số lượng nhiều nhất kho")
    _tacvu=input("Nhập tác vụ muốn thực hiện")
    if _tacvu == "1":
        # pass
        _noidung = read_file(_path)
        print_file(_noidung)
    elif _tacvu =="2":
        pass
    elif _tacvu =="3":
        pass
    elif _tacvu =="4":
        pass
    elif _tacvu =="5":
        # pass
        _noidung = read_file(_path)
        _result = tim_lon_nhat(_noidung)
        print_file(_result)
        
    else:
        print("Thoát khỏi chương trình")
        break