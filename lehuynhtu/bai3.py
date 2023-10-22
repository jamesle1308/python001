# the quick brown for jumps over the lazy dog
#  HELLO MY CLASS

_bangchucai = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]
_chuoi = input("Chuỗi cần kiểm tra: ")
_lowerchuoi = _chuoi.lower()
_lstchuoi = list(_lowerchuoi)
_lenChuoi = len(_lstchuoi)
_lenChuoi = len(_bangchucai)
print(_lstchuoi)
print(_bangchucai)
print(_lenChuoi)

while True:
    if _lenChuoi > 25:
        break
for i in _bangchucai:
    if i not in _lstchuoi:
        print(i)
        print(_chuoi," không phải là chuỗi PANGGRAM")
        break
else:
    print(_chuoi," là chuỗi PANGGRAM")