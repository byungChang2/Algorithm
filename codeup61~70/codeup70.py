"""
월이 입력될 때 계절 이름이 출력되도록 해보자.
월 : 계절 이름
12, 1, 2 : winter
3, 4, 5 : spring
6, 7, 8 : summer
9, 10, 11 : fall
"""

d = input()
if d =='1' or d =='2' or d =='12':
  print("winter")
elif d =='3' or d =='4' or d =='5':
  print("spring")
elif d =='6' or d =='7' or d =='8':
  print("summer")
elif d =='9' or d =='10' or d =='11':
  print("fall")  