#정수 3개 입력받아 합,평균을 출력
a,b,c = map(int,input().split())
x=a+b+c
x1=float(x)/3
print(x,format(x1,".2f"))