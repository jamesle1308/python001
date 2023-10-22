# Tuần 4 bài 5
from libs.functions import *
_path = "files/donhang.csv"
while True:
    print("Quản lý đơn hàng")
    print("1: In dữ liệu đơn hàng")
    print("2: Thêm đơn hàng mới vào file")
    print("3: Thống kê xem mỗi đơn hàng đã mua tổng số lượng và tổng giá trị là bao nhiêu?")
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
        _noidung.pop(0)
        _tempSet = set()
        for _row in _noidung:
            _tempSet.add(_row[0])
        print("{:20}|{:20}|{:20}".format("Mã ĐH","SL","Thành Tiền"))
        
        for _maDH in sorted(_tempSet):
            thong_ke(_maDH,_noidung)
        
        #giống bài tính điểm trung bình project4
        #tạo 1 set trước để loại bỏ trùng rồi dò trong set dùng vòng lặp cộng lại
    else:
        print("Thoát khỏi chương trình")
        break

