_laisuat=float(input('lãi suất năm: '))
_tiengui=float(input('tiền gửi: '))
_sothanggui=int(input('số tháng gửi: '))
#phía sau % phải xác định được kiểu dữ liệu là gì thì nó mới thực hiện chức năng được
print('Tiền lãi = %i'%(_tiengui*_sothanggui*_laisuat/12))
print('Tổng số tiền = ',_tiengui+_tiengui*_laisuat)