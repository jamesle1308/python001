from libs.functions import *
_path = "files/madinhdanh.csv"
while True:
    print("Thao tác với file CSV")
    print("1: In dữ liệu tập tin CSV")
    print("2: Thêm dữ liệu vào file CSV")
    print("3: Cập nhật dữ liệu file CSV theo mã định danh")
    print("4: Xóa dữ liệu vào file CSV")
    print("5: Tìm kiếm và thống kê")
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
        # pass
        _noidung = read_file(_path)
        _noidungUpdate = update_new(_noidung)
        write_file(_path,_noidungUpdate)
    elif _tacvu =="4":
        # pass
        _noidung = read_file(_path)
        _noidungDelete = delete_new(_noidung)
        write_file(_path,_noidungDelete)
    elif _tacvu =="5":
        # pass
        _noidung = read_file(_path)
        _thongke = thong_ke(_noidung)
        print("Có",len(_thongke),"được tìm thấy")
        if len(_thongke)>0:
            # for _row in _thongke:
            #     print("{:20}{:30}{:20}{:20}{:20}{:20}{:20}".format(_row[0],_row[1],_row[2],_row[3],_row[4],_row[5],_row[6]))
            print_file(_thongke)
        else:
            print("Ko tìm thấy")
    else:
        print("Thoát khỏi chương trình")
        break