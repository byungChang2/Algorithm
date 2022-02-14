"""
평가를 문자(A, B, C, D, ...)로 입력받아 내용을 다르게 출력해보자.

평가 내용
평가 : 내용
A : best!!!
B : good!!
C : run!
D : slowly~
나머지 문자들 : what?
"""

a = input()
print("best!!!") if a=='A' else print("good") if a =='b' else print("run!") if a =='C' else print("slowly") if a == 'D' else print("what?")
"""if a == 'A':
  print("best!!!")
elif a == 'B':
  print("good!!")
elif a == 'C':
  print("run!")
elif a == 'D':
  print("slowly~")  
else:
  print("What?")"""