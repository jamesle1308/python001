while True:
    _so=int(input("Nhập một số để kiểm tra: "))
    if _so>0:
        break
_tonguoc=0
print("Các ước: ")
for i in range(1,_so):
    if _so%i ==0:
        _tonguoc +=i
        print(i, end=",")
print("\n")
if _tonguoc ==_so:
    print("Số này là số hoàn hảo")
else:
    print("Số này fail rồi")