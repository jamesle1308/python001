while True:
    _so=int(input("Nhập một số để kiểm tra: "))
    if _so>1:
        break
if _so==2:
    print("2 là số nguyên tố")
else:
    for i in range(2,_so):
        if _so%i:
            print(_so," không phải là số nguyên tố")
            break
    else:
        print(_so," là SNT")