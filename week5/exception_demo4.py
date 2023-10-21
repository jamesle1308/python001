class LoiChiaSo(ZeroDivisionError):
    def __init__(self, thongbao) -> None:
        self.thongbao = thongbao
def thuong(a,b):
    try:
        if b==0:
            raise LoiChiaSo("Lỗi chia số 0, số thứ 2 phải khác 0")
        thuong = a/b
    except LoiChiaSo as err:
        print(err)
    else:
        print("thương: ", thuong)
thuong(5,0)
thuong(10,2)    