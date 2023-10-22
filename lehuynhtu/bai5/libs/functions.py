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


def update_new(_content):
    _username = input("Nhập username: ")
    _password = input("Nhập password: ")
    for _row in _content:
        if _row[1] ==_username and _row[2]== _password:
            print("đăng nhập thành công")
            _stt = _row[0]
            _userN = _row[1]
            _pass = _row[2]
            _lName = _row[3]
            _fName = _row[4]
            _rqUpdatepass = input("Nhấn Y nếu muốn cập nhật pass mới: ")
            if _rqUpdatepass == "y":
                _passWord = input("Nhập mật khẩu mới: ")
                while True:
                    if len(_passWord) >= 8:
                        break
            _pass = _passWord
            _row[0] = _stt
            _row[1] = _userN
            _row[2] = _pass
            _row[3] = _lName
            _row[4] = _fName
            _row[5] = datetime.now()
            print("Update thành công")
    else:
        print("Đăng nhập không thành công")            
    return _content

def write_file(_path,_content):
    f=open(_path,"w",encoding="utf-8",newline="") #Ko có newline ="" => lỗi tè lè, do ko có dữ liệu thì ctr chính đâu có đọc được đâu
    csv.writer(f).writerows(_content)
    f.close()
    return #return rỗng thì không cần cũng được
    
