# Bài 8: Quản lý gói cước di động
# Yêu cầu :
# -     Khởi tạo thông tin của các gói cước di dộng : goi_cuoc={'D3':[15000,3,3],'DT30':[30000,7,7],'M50':[50000,1.2,30]}
# -     Cho phép người dùng chọn các chức năng tương ứng từ danh mục :
# ·       Người dùng chọn chức năng 1: xem các gói cước (mã gói, giá, dung lượng, thời hạn) đang được lưu
# trữ trên hệ thống (in dữ liệu thành các cột).
# ·       Người dùng chọn chức năng 2: thêm gói cước mới vào hệ thống (mỗi gói có một mã duy nhất không
# được trùng nhau).
# ·       Người dùng chọn chức năng 3: cập nhật lại thông tin gói cước thông qua mã gói (thông báo không
# cập nhật được nếu mã gói không tồn tại), nhấn 1 để quyết định thông tin nào cần cập nhật.
# ·       Người dùng chọn chức năng 4: tính dung lượng/ngày của các gói cước;
# ·       Nếu người dùng chọn các chức năng khác 4 chức năng trên thì thông báo tác vụ sai và thoát khỏi chương trình.
############ Các Hàm Xử Lý ##############
def _xemGoiCuoc(_duLieu):
    print("{:10}{:10}{:10}{:10}".format("Mã Gói","Giá","DL","Thời Hạn"))
    for k,v in _duLieu.items():
        print("{:10}{:10}{:10}{:10}".format(k,v[0],v[1],v[2]))

############ Chương trình chính ##############
goi_cuoc={'D3':[15000,3,3],'DT30':[30000,7,7],'M50':[50000,1.2,30]}
while True:
    print("CHƯƠNG TRÌNH QUẢN LÝ GÓI CƯỚC")
    print("1: Xem gói cước")
    print("2: Thêm gói cước")
    print("3: Cập nhật gói cước")
    print("4: Tính DL/ngày của gói cước")
    _tacvu=input("Nhập tác vụ muốn thực hiện")
    if _tacvu =="1":
        _xemGoiCuoc(goi_cuoc)
    elif _tacvu =="2":
        pass
    elif _tacvu =="3":
        pass
    elif _tacvu =="4":
        pass
    else:
        print("Thoát khỏi chương trình")
        break