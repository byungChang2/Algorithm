'''
day는 날 수, a/b/c는 방문 주기이다.
'''
a,b,c= map(int,input().split())
d=1
while d%a!=0 or d%b!=0 or d%c!=0:
  d+=1
  if d%a==0 and d%b==0 and d%c==0:
    print(d)
    break
    