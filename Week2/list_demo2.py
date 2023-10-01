#for i in range(start,stop,step)
# start => ko điền hệ thống tự hiểu là 0
# step => Không điền hệ thống tự hiệu là 1
# Stop bắt buộc điền để hệ thống biết điểm dừng để ko gặp vòng lăp vô hạn
import random
_listRandom = []
for i in range(5):
    x = random.randint(0,100)
    _listRandom.append(x)
print("Một list random từ 0-100 sẽ là: ",_listRandom)