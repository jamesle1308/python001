# Bài 9:
#  Xây dựng các hàm:
# - Nhập username và password của tài khoản vào hệ thống (password phải từ 8 kí tự trở lên);
# - Xem danh sách username và password tương ứng;
# - Cập nhật username và password (nhập pass cũ trước khi tạo pass mới);
# - Xóa username và password;
# Xây dựng chương trình chọn và thực hiện chức năng tương ứng từ hàm đã xây dựng;
# Dữ liệu khởi tạo: tai_khoan={'user01':'abc@123'}

############ Các Hàm Xử Lý ##############
# def  _dangnhap(_u):

############ Chương trình chính ##############
tai_khoan={'user01':'abc@123'}
while True:
    print("DASHBOARD TÀI KHOẢN")
    print("1: ĐĂNG NHẬP")
    print("2: DANH SÁCH USERS")
    print("3: CẬP NHẬT USERNAME & PASSWORD")
    print("4: XÓA USERNAME & PASSWORD")
    _tacvu=input("Nhập tác vụ muốn thực hiện")
    if _tacvu =="1":
        # pass
        _u =input("Nhập tên đăng nhập vào")
        pass
    elif _tacvu =="2":
        pass
    elif _tacvu =="3":
        pass
    elif _tacvu =="4":
        pass
    else:
        print("Thoát khỏi chương trình")
        break