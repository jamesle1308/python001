def  tinh_dtb(hk1,hk2):
    assert(hk1>0 and hk2>0), "Điểm TB phải >0"
    return(hk1+hk2*2)/3
hk1, hk2 = eval(input("nhập điểm trung bình HK1 và HK2 theo thứ tự: "))
dtb = tinh_dtb(hk1,hk2)
print("Điểm trung bình năm học: ",dtb)
    