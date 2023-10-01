# Bài 11: Tìm thú trong vườn thú:
# - Tạo ra một list tên có các con thú: animal_name;
# - Nhập vào tên 1 con thú cần tìm: search_name
# - Trả kết quả có tìm thấy được hay không? Nếu tìm thấy thì tìm thấy mấy lần?
_animalName=["bear", "bee", "dog", "cat", "mouse", "fly", "zibra", "horse"]
_searhName = input("Nhập tên động vật muốn tìm vào đây:")
_lowSearchName = _searhName.lower().strip()
# Lệnh strip() ko điền giá trị sẽ xoa khoảng trắng 2 đầu
if _lowSearchName in _animalName:
    _soLanXuatHien=_animalName.count(_lowSearchName)
    print(_lowSearchName,"Xuất hiện",_soLanXuatHien,"lần")
else:
    print(_lowSearchName,"không tồn tại trong danh sách này")