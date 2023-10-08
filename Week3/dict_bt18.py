input_str=input("Nhập một câu để xử lý: ")
# về nhà làm tiếp
_lisWword=input_str.split() #Chuyển kiểu chuỗi thành kiểu List
_setWord = set(_lisWword)
_sortSetWord=sorted(_setWord)
print("Các từ sau khi sắp xếp: ",_sortSetWord)
_numWord = len(_sortSetWord) #Đếm số phần tử của kiểu set
_numChar = 0
for _word in _sortSetWord:
    _numChar += len(_word)
print("Số phần từ của tập Set là ",_numWord)
print("Số ký tự của tập Set là ",_numChar)