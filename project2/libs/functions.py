import csv
from datetime import datetime
def read_file(_path):
    f=open(_path,"r",encoding="utf-8")
    _content=[]
    for _row in csv.reader(f):
        _content.append(_row)
    f.close()
    return _content

def print_file(_content):
    for _row in _content:
        print("{:20}{:30}{:20}{:20}{:20}{:20}{:20}".format(_row[0],_row[1],_row[2],_row[3],_row[4],_row[5],_row[6]))


def add_new(_content):
    _maDinhDanh = input("Nhập mã định danh mới: ")
    for _row in _content:
        if _row[0]== _maDinhDanh:
            print("Mã định danh này đã tồn tại trong hệ thống")
            break #break để thoát vòng lặp cho user điền lại
    else:
        _ten = input("Nhập tên: ")
        _userName = input("Nhập username ")
        _passWord = input("Nhập mật khẩu ")
        _gT = input("Nhập giới tính ")
        _boPhan = input("Nhập bộ phận ")
        _dateInput = datetime.now()
        _content.append([_maDinhDanh,_ten,_userName,_passWord,_gT,_boPhan,_dateInput])
        print("THÊM THÀNH CÔNG")
    return _content

def update_new(_content):
    _maDinhDanh = input("Nhập mã định danh: ")
    for _row in _content:
        if _row[0] ==_maDinhDanh:
            print("mã định danh này có tồn tại")
            _ten = _row[1]
            _userName = _row[2]
            _passWord = _row[3]
            _gT = _row[4]
            _boPhan = _row[5]
            _rqUpdateName = input("Nhấn Y nếu muốn cập nhật mới")
            if _rqUpdateName == "y":
                _ten = input("Nhập tên mới: ")
            _rqUpdateUserName = input("Nhấn Y nếu muốn cập nhật username mới")
            if _rqUpdateUserName == "y":
                _userName = input("Nhập username mới: ")
            _rqUpdatepass = input("Nhấn Y nếu muốn cập nhật pass mới")
            if _rqUpdatepass == "y":
                _passWord = input("Nhập mật khẩu mới: ")
            _rqUpdateGT = input("Nhấn Y nếu muốn cập nhật giới tính mới")
            if _rqUpdateGT == "y":
                _gT = input("Nhập giới tính mới: ")
            _rqUpdateBoPhan = input("Nhấn Y nếu muốn cập nhật bộ phận mới")
            if _rqUpdateBoPhan == "y":
                _boPhan = input("Nhập tên bộ phận mới: ")
            _row[1] = _ten
            _row[2] = _userName
            _row[3] = _passWord
            _row[4] = _gT
            _row[5] = _boPhan
            _row[6] = datetime.now()
    else:
        print("Mã định danh này không tồn tại trong hệ thống")
    return _content

def delete_new(_content):
    _maDinhDanh = input("Nhập mã định danh: ")
    for _row in _content:
        if _row[0] ==_maDinhDanh:
            _content.remove(_row)
            break
    else:
        print("Mã định danh này không tồn tại trong hệ thống")
    return _content

def thong_ke(_content):
    _boPhan = input("Nhập bộ phận muốn tìm kiếm")
    _result = []
    for row in _content:
        if row[5] == _boPhan:
            print("Tìm thấy rồi nha")
            _result.append(row)
    else:
        print("Không tìm thấy rồi")
    return _result

def write_file(_path,_content):
    f=open(_path,"w",encoding="utf-8",newline="") #Ko có newline ="" => lỗi tè lè, do ko có dữ liệu thì ctr chính đâu có đọc được đâu
    csv.writer(f).writerows(_content)
    f.close()
    return #return rỗng thì không cần cũng được
    
