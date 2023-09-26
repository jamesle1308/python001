# Bài 16:
# Viết chương trình xếp loại năng lực dựa trên điểm trung bình biết:
# <3.5: Kém
# 3.5 - <5.0: Yế
# 5.0 - <6.5: Trung bình
# 6.5 - <8.0: Khá
# >=8.0: Giỏi
_dtb=float(input('nhập đtb của học sinh: '))
if _dtb <3.5:
    print('học sinh kém')
elif 3.5<_dtb<5.0:
    print('học sinh yếu')
elif 5.0<_dtb<6.5:
    print('học sinh trung bình')
elif 6.5<_dtb<8.0:
    print('học sinh khá')
else:
    print('Học sinh giỏi')