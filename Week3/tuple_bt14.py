#### chép lại bài tập trong điện thoại ra
import calendar
_strDay=input("Nhập ngày kiểm tra")
_lstDay=_strDay.split("/")
_ngay=int(_lstDay[0])
_thang=int(_lstDay[1])
_nam=int(_lstDay[2])
_tupDay='Thứ 2','Thứ 3','Thứ 4','Thứ 5','Thứ 6','Thứ 7','Chủ nhật'
_thu=_tupDay[calendar.weekday(_nam,_thang,_ngay)]
print('Ngay {} là {}'.format(_strDay,_thu))