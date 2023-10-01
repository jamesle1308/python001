while True:
    n= int(input("Nhập 1 số count down: "))
    if n>0:
        break
    else:
        print("vui lòng nhập một số >0")
for i in range (1,n+1,2):
    print(i, end="-")
