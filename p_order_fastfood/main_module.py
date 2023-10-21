# Tuần 4 bài 5
from libs.functions import *
_path = "files/donhang.csv"
while True:
    print("Quản lý đơn hàng")
    print("1: In dữ liệu đơn hàng")
    print("2: Thêm đơn hàng mới vào file")
    print("2: Thống kê xem mỗi đơn hàng đã mua tổng số lượng và tổng giá trị là bao nhiêu?")
    _tacvu=input("Nhập tác vụ muốn thực hiện: ")
    if _tacvu == "1":
        # pass
        _noidung = read_file(_path)
        print_file(_noidung)
    elif _tacvu == "2":
        # pass
        _noidung = read_file(_path)
        _newOrder = new_order(_noidung)
        write_file(_path,_newOrder)   
    elif _tacvu == "3":
        # pass    
        _noidung = read_file(_path)
        _thongke = thong_ke(_noidung)
        print(_thongke)
        #giống bài tính điểm trung bình project4
        #tạo 1 set trước để loại bỏ trùng rồi dò trong set dùng vòng lặp cộng lại
    else:
        print("Thoát khỏi chương trình")
        break

