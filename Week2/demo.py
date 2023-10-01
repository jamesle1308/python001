# Tuần 2, làm quen với vòng lặp while for

n= int(input("Nhập 1 số count down: "))
"""
while n>0:
    print(n)
    n-=1
    """
for i in range (n,0,-1):
    print(i)
for i in range (1,n+1,2):
    print(i, end="-")
