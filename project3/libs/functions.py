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
        print("{:20}{:30}{:20}{:20}{:20}{:20}".format(_row[0],_row[1],_row[2],_row[3],_row[4],_row[5]))


def add_new(_content):
    _maSV = input("Nhập mã sinh viên mới mới: ")
    for _row in _content:
        if _row[0]== _maSV:
            print("Mã định danh này đã tồn tại trong hệ thống")
            break #break để thoát vòng lặp cho user điền lại
    else:
        _ten = input("Nhập tên sinh viên mới: ")
        _maMonHoc = input("Nhập mã môn học ")
        _tenMonHoc = input("Nhập tên môn học ")
        _diem = input("Nhập điểm ")
        _dateInput = datetime.now()
        _content.append([_maSV,_ten,_maMonHoc,_tenMonHoc,_diem,_dateInput])
        print("THÊM THÀNH CÔNG")
    return _content

def update_new(_content):
    _maSV = input("Nhập mã định danh: ")
    for _row in _content:
        if _row[0] ==_maSV:
            print("mã sinh viên này có tồn tại")
            _ten = _row[1]
            _maMonHoc = _row[2]
            _tenMonHoc = _row[3]
            _diem = _row[4]
            _rqUpdateName = input("Nhấn Y nếu muốn cập nhật tên mới")
            if _rqUpdateName == "y":
                _ten = input("Nhập tên mới: ")
            _rqUpdateMaMon = input("Nhấn Y nếu muốn cập nhật mã môn học mới")
            if _rqUpdateMaMon == "y":
                _maMonHoc = input("Nhập username mới: ")
            _rqUpdateTenMonHoc = input("Nhấn Y nếu muốn cập nhật tên môn học mới")
            if _rqUpdateTenMonHoc == "y":
                _tenMonHoc = input("Nhập mật khẩu mới: ")
            _rqUpdateDiem = input("Nhấn Y nếu muốn cập nhật điểm mới")
            if _rqUpdateDiem == "y":
                _diem = input("Nhập điểm mới: ")
            _row[1] = _ten
            _row[2] = _maMonHoc
            _row[3] = _tenMonHoc
            _row[4] = _diem
            _row[5] = datetime.now()
    else:
        print("Mã sinh viên này không tồn tại trong hệ thống")
    return _content

def delete_new(_content):
    _maSV = input("Nhập mã sinh viên: ")
    for _row in _content:
        if _row[0] ==_maSV:
            _content.remove(_row)
            break
    else:
        print("Mã định danh này không tồn tại trong hệ thống")
    return _content

def thong_ke(_content):
    _maMH = input("Nhập mã môn học cần kiểm tra")
    _tieuDe =_content.pop(0) #lệnh pop sẽ xóa và trả lại giá trị đã xóa
    _result = [_tieuDe]
    for row in _content:
        if float(row[4]) < 5 and row[3]==_maMH:
            print("Tìm thấy rồi nha")
            _result.append(row)
    else:
        print("Không tìm thấy rồi")
    return _result

def tinh_dtb(_maMH,_content):
    _soLuong = 0
    _tongDiem = 0
    for _row in _content:
        if _row[2] == _maMH:
            _soLuong += 1
            _tongDiem += float(_row[4])
    print("{:10}|{:10}".format(_maMH,str(_tongDiem/_soLuong)))
    return #return rỗng -> bỏ cũng đc


def write_file(_path,_content):
    f=open(_path,"w",encoding="utf-8",newline="") #Ko có newline ="" => lỗi tè lè, do ko có dữ liệu thì ctr chính đâu có đọc được đâu
    csv.writer(f).writerows(_content)
    f.close()
    return #return rỗng thì không cần cũng được
    
