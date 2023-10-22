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

def write_file(_path,_content):
    f=open(_path,"a",encoding="utf-8",newline="") #Ko có newline ="" => lỗi tè lè, do ko có dữ liệu thì ctr chính đâu có đọc được đâu
    csv.writer(f).writerows(_content)
    f.close()
    return

def new_order(_orders):
    _lastOrder = _orders[-1] #lấy đơn hàng cuối cùng
    _orderCode = _lastOrder[0] #lấy phần tử đầu tiên là mã đơn của đơn hàng cuối cùng là một số thứ tự
    _orderCodeNew = int(_orderCode) + 1
    _newOrder= []
    _type = {
        "1": ["Gà rán",45000,"miếng"],
        "2": ["Cola",14000,"chai"],
        "3": ["Khoai Tây",45000,"gram"],
        "4": ["Xiên que",15000,"que"],
    }
    while True:
        _action = input("Nhập y nếu muốn tiếp tục order: ")
        if _action == "y":
            _whichType = input("[1. Gà Rán, 2. Cola, 3. Khoai Tây, 4. Xiên que] chọn theo danh sách sau")
            if _whichType == "1":
                _tempOrder = _type["1"]
            elif _whichType == "2":
                _tempOrder = _type["2"]
            elif _whichType == "3":
                _tempOrder = _type["3"]
            elif _whichType == "4":
                _tempOrder = _type["4"]
            _typeName = _tempOrder[0]
            _typeUnitPrice = _tempOrder[1]
            _typePiece = _tempOrder[2]
            _howMany = int(input("Nhập số lượng muốn order: "))
            _orderPrice = _typeUnitPrice * _howMany
            _orderDate = datetime.now()
            _orderInfo = [_orderCodeNew, _typeName, _howMany, _typePiece, _typeUnitPrice, _orderPrice, _orderDate]
            _newOrder.append(_orderInfo)
        else:
            break
    return _newOrder #ngang cấp vs while để ko break vòng lặp khi muốn đặt nhiều món trong 1 order

def thong_ke(_tempSet,_content):
    _sl=0
    _thanhtien = 0
    for _r1 in _content:
        if _r1[0] == _tempSet:
            _madon = _r1[0]
            _sl += float(_r1[2])
            _thanhtien += float(_r1[5])
    print("{:20}|{:20}|{:20}".format(_madon,_sl,_thanhtien))
    return

