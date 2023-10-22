from libs.functions import *
_path = "files/account.csv"
while True:
    print("QUẢN LÝ TÀI KHOẢN")
    print("1: Xem toàn bộ các tài khoản đang lưu trên file")
    print("2: Đổi mật khẩu cho một tài khoản với điều kiện")
    _tacvu=input("Nhập tác vụ muốn thực hiện")
    if _tacvu == "1":
        # pass
        _noidung = read_file(_path)
        print_file(_noidung)
    elif _tacvu =="2":
        # pass
        _noidung = read_file(_path)
        _noidungMoi = update_new(_noidung)
        write_file(_path,_noidungMoi)
    else:
        print("Thoát khỏi chương trình")
        break