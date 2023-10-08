# Bài 3: nhập vào số hạng đầu tiên U0, công sai d và xuất ra n số hạng đầu tiên của dãy cấp số cộng.
def _tinhCsc (u0,d,n):
    _lstSo = [u0]
    for i in range(1,n):
        _so = _lstSo[i-1] + d
        _lstSo.append(_so)
    return _lstSo
n = int(input("Nhập số phần tử"))
d = int(input("Nhập công sai"))
u0 = int(input("Nhập số hạng mở đầu"))
_lstCsc = _tinhCsc(u0,d,n)
print("Dãy số hạng sẽ là",str(_lstCsc))