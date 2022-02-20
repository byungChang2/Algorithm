###w, h, b 가 공백을 두고 입력된다.
###단, w, h는 모두 정수이고 1~1024 이다. b는 40이하의 4의 배수이다.
w,h,b =map(int,input().split())
print(round(w*h*b/8/1024/1024, 2),"MB")
