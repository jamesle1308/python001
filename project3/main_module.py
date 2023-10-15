from libs.functions import *
_path = "files/diem.csv"
while True:
    print("Quản lý sinh viên")
    print("1: In dữ liệu Sinh Viên")
    print("2: Thêm sinh viên mới")
    print("3: Cập nhật thông tin sinh viên theo mã sinh viên")
    print("4: Xóa sinh viên ra khỏi danh sách")
    print("5: Tìm kiếm danh sách các bạn sinh viên bị rớt môn thông qua tên môn (kết quả <5 là rớt)")
    print("6: Tính điểm trung bình của môn học")
    _tacvu=input("Nhập tác vụ muốn thực hiện")
    if _tacvu == "1":
        # pass
        _noidung = read_file(_path)
        print_file(_noidung)
    elif _tacvu =="2":
        # pass
        _std = read_file(_path)
        _stdNew = add_new(_std)
        write_file(_path,_stdNew)
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
        print("Có",len(_thongke)-1," sinh viên được tìm thấy")
        if len(_thongke)>1: #có tiêu đề nên mới để >1 - Ko có tiêu đề thì >0
            # for _row in _thongke:
            #     print("{:20}{:30}{:20}{:20}{:20}{:20}{:20}".format(_row[0],_row[1],_row[2],_row[3],_row[4],_row[5],_row[6]))
            print_file(_thongke)
        else:
            print("Ko tìm thấy")
    elif _tacvu =="6":
        # pass
        _noidung = read_file(_path)
        _noidung.pop(0)
        _SetmaMH = set()
        for _row in _noidung:
            _SetmaMH.add(_row[2])
        # _sortMaMH = sorted(_maMH) #Săp sếp theo thứ tự thôi ko cần cũng đc
        print("{:10}|{:10}".format("Mã MH","ĐTB"))
        for _maMH in _SetmaMH:
            tinh_dtb(_maMH,_noidung)
    else:
        print("Thoát khỏi chương trình")
        break