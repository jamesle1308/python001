# Bài 4: Dãy Fibonacci là dãy vô hạn các số tự nhiên bắt đầu bằng hai phần 0 và 1, các phần tử sau đó được
# thiết lập theo quy tắc mỗi phần tử luôn bằng tổng hai phần tử trước nó.
# Viết chương trình in ra dãy Fibbonacci gồm n số hạng đầu tiên.
def _tinhfb (n):
    _lstSo = [0,1]
    for i in range(2,n):
        _so = _lstSo[i-1] + _lstSo[i-2]
        _lstSo.append(_so)
    return _lstSo

n = int(input("Nhập số phần tử"))
_dayfb = _tinhfb(n)
print("dãy fb là", str(_dayfb))