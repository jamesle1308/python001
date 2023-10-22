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
        print("{:20}{:30}{:20}".format(_row[0],_row[1],_row[2]))

def tinh_dtb(_maMH,_content):
    _soLuong = 0
    _tongDiem = 0
    for _row in _content:
        # print(_row[1])
        # print(_row[2])
        # print(type(float(_row[2])))
        if _row[1] == _maMH:
            _soLuong += 1
            _tongDiem += float(_row[2])
    # print(_soLuong)        
    # print(_tongDiem)        
    print("{:10}|{:10}|{:10}".format(_maMH,_soLuong,str(_tongDiem/_soLuong)))
    return #return rỗng -> bỏ cũng đc

    
