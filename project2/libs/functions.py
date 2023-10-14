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

def write_file(_path,_content):
    f=open(_path,"w",encoding="utf-8")
    csv.writer(f).writerows(_content)
    f.close()
    return #return rỗng thì không cần cũng được
    
