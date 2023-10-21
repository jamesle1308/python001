try:
    a = float(input("Nhập số bị chia: "))
    b = float(input("Nhập số chia: "))
    print("thương: %.1f"%(a/b))
except ZeroDivisionError as er2:
    print("Lỗi chia cho số 0")
finally:
    print("Tổng: ", a+b)
    print("Hiệu: ", a-b)
    print("Tích: ", a*b)
    