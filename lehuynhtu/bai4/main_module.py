# Cài đặt và cho phép người dùng chọn các chức năng tương ứng từ danh mục :
# - Người dùng chọn chức năng 1: xem thông tin kết quả học tập;
# - Người dùng chọn chức năng 2: thống kê số sinh viên theo môn học và tính điểm trung
# bình cho từng môn;

from libs.functions import *
_path = "files/qlsv.csv"
while True:
    print("Quản lý điểm thi sinh viên")
    print("1: xem thông tin kết quả học tập")
    print("2: thống kê số sinh viên theo môn học và tính điểm trung bình cho từng môn")
    _tacvu=input("Nhập tác vụ muốn thực hiện")
    if _tacvu == "1":
        # pass
        _noidung = read_file(_path)
        print_file(_noidung)
    elif _tacvu =="2":
        # pass
        _noidung = read_file(_path)
        _noidung.pop(0)
        _setMaMon = set()
        for i in _noidung:
            _setMaMon.add(i[1])
        print(_setMaMon)
        print("{:10}|{:10}|{:10}".format("Mã MH","SL","ĐTB"))
        for _maMH in _setMaMon:
            tinh_dtb(_maMH,_noidung)
    else:
        print("Thoát khỏi chương trình")
        break
    