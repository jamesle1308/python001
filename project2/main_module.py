from libs.functions import *
_path = "files/madinhdanh.csv"
while True:
    print("Thao tác với file CSV")
    print("1: In dữ liệu tập tin CSV")
    print("2: Thêm dữ liệu vào file CSV")
    print("3: Thống kê đơn giản")
    _tacvu=input("Nhập tác vụ muốn thực hiện")
    if _tacvu == "1":
        # pass
        _noidung = read_file(_path)
        print_file(_noidung)
    elif _tacvu =="2":
        # pass
        _noidung = read_file(_path)
        _noidungMoi = add_new(_noidung)
        write_file(_path,_noidungMoi)
    elif _tacvu =="3":
        pass
    else:
        print("Thoát khỏi chương trình")
        break