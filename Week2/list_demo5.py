_diemSinhVien = [["sv01","tule","10"],["sv02","nhioanh","8"],["sv03","kimanh","9"]]
print("{:10}{:10}{:10}".format("Ma SV","Ten SV", "Diem SV"))
for i in _diemSinhVien:
    print("{:10}{:10}{:10}".format(i[0],i[1],i[2]))