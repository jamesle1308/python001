while True:
    n = int(input("Nhập điểm dừng: "))
    if n>2:
        break
    else:
        print("Nhập 1 số lớn hơn 2")
for i in range(1,10):
    for j in range (2,n+1):
        print("{}x{}={}".format(i,j,i*j),end="\t")
    print("\n")
    