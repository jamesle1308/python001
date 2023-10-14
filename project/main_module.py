from libs.functions import *
_path = "files/QueHuong.txt"
while True:
    print("Thao tác với file")
    print("1: In dữ liệu tập tin")
    print("2: Thêm dữ liệu vào file")
    print("3: Thống kê đơn giản")
    _tacvu=input("Nhập tác vụ muốn thực hiện")
    if _tacvu == "1":
        # pass
        _noidung = read_file(_path)
        print(_noidung)
    elif _tacvu =="2":
        # pass
        write_file(_path)
    elif _tacvu =="3":
        # pass
        _numRow, _numWord, _numChar = thong_ke(_path)
        print("Số dòng ",_numRow)
        print("Số Từ ",_numWord)
        print("Số kí từ ",_numChar)
    else:
        print("Thoát khỏi chương trình")
        break