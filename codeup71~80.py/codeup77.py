#짝수 합 구하기(설명)(py)
#정수(1 ~ 100) 1개를 입력받아 1부터 그 수까지 짝수의 합을 구해보자.
a = int(input())
s=0
for i in range(a+1):
  if i%2==0:
    s+=i
print(s)