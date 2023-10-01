# Bài 13: Cho list gốc: or_lst=[1,5,8,-1,2,6,0,-8,-6,11,19,21,3]
# Tạo new_list bằng cách tăng mỗi phần tử của or_list lên 2 đơn vị;
# Tạo new_list bằng cách lọc ra các phần tử âm trong or_list;
# Tạo new_list bằng cách thay các phần tử âm bằng 0;
or_lst=[1,5,8,-1,2,6,0,-8,-6,11,19,21,3]
# Cấu trục list comprehension (hoàn hảo)
# Bảo tổn phần tử nhưng chỉ thay đổi giá trị
_list1=[x+2 for x in or_lst]
print(_list1)
# Lọc ra các phần tử lớn hơn 0
_list2=[x for x in or_lst if x<0]
print(_list2)
# Thay thế phần tử không thỏa điều kiện
_list3=[x if x>0 else 0 for x in or_lst]
print(_list3)