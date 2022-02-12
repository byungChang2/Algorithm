# 3,-1,5
a, b, c = map(int,input().split())
print((a if a<b else b)if((a if a< b else b)<c)else c)
