try:
    a = float(input("Nhập số bị chia: "))
    b = float(input("Nhập số chia: "))
    thuong = a/b
    print("thương: ", thuong)
except ZeroDivisionError as er:
    print("Lỗi chia cho số 0")