def read_file  (_path):
    f = open(_path,mode="r",encoding="utf-8")
    _content = f.read()
    f.close()
    return _content

def write_file  (_path):
    f = open(_path,mode="a",encoding="utf-8")
    _newContent = "\n"
    _newContent += input("Nhập nội dung mới vào đây ")
    f.write(_newContent)
    print("Thêm thành công")
    f.close()
    return 

def thong_ke  (_path):
    f = open(_path,mode="r",encoding="utf-8")
    # _content = f.read() --- này là dùng function read thì chuyển về kiểu string rồi-> vòng lặp vào đây là sai bét rồi -> chuyển kiểu về String rồi ko duyệt vòng lặp được
    _soDong, _soTu, _soKiTu = 0,0,0
    for _row in f:
        _soDong += 1
        _lstSoTu = _row.split()
        _soTu += len(_lstSoTu)
        _soKiTu += len(_row)
    f.close()
    return _soDong, _soTu, _soKiTu

