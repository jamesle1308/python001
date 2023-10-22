def day_lucas (u0,u1,n):
    lst_so=[u0,u1]
    for i in range (2,n):
        so=lst_so[i-2] + lst_so[i-1]
        lst_so.append(so)
    return lst_so
n=int(input('Nhap diem dung cua day Lucas: '))
u0=0
u1=1
lst_lucas=day_lucas(2,1,n)
print('Day cac so Lucas gom {} so hang la {}'.format(n,str(lst_lucas)))