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
        print("{:20}{:20}{:20}{:20}{:20}{:20}{:20}".format(_row[0],_row[1],_row[2],_row[3],_row[4],_row[5],_row[6]))

def tim_lon_nhat(_content):
    _tieude = _content.pop(0)
    _max=0
    _dongLonNhat = []
    for _row in _content:
        if _max < int(_row[2]):
            _max=int(_row[2])
            _dongLonNhat=_row
    _result=[_tieude,_dongLonNhat]
    return _result

def write_file(_path,_content):
    f=open(_path,"w",encoding="utf-8",newline="") #Ko có newline ="" => lỗi tè lè, do ko có dữ liệu thì ctr chính đâu có đọc được đâu
    csv.writer(f).writerows(_content)
    f.close()
    return #return rỗng thì không cần cũng được
    
