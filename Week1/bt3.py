_tenhang=input('Sản phẩm tên là: ')
_soluong=int(input('Số lượng: '))
_dongia=float(input("Giá bán: "))
#dấu  2 chấm có nhiều nghĩa, ưu tiên hoặc thông báo một giá trị số sắp xuất hiện, xử lý các kiểu dữ liệu liên quan đến kiểu int, thường đi kèm với các cách xử lý số liệu như lấy số thập phân
print('Tổng tiền cần thanh toán cho {:} là {}*{:,}={:,} VNĐ'.format(_tenhang,_soluong,_dongia,_soluong*_dongia))