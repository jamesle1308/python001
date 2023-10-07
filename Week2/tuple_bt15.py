_can="Canh","Tân","Nhâm","Quý","Giáp","Ất","Bính","Đinh","Mậu","Kỷ"
_chi="Thân","Dậu","Tuất","Hợi","Tý","Sửu","Dần","Mão","Thìn","Tỵ","Ngọ","Mùi"
_namDuongLich=int(input("Nhập năm dương lịch"))
while True:
    if _namDuongLich>0:
        break
    else:
        print("Nhập lại năm dương lịch cho đúng")
_namCan=_can[_namDuongLich%10]
_namChi=_chi[_namDuongLich%12]
_namAmLich= _namCan+" "+_namChi
print(_namAmLich)
