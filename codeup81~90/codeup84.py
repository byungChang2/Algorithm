r,g,b =map(int,input().split())

i=0
j=0
z=0
count = 0
for i in range(r):
  for j in range(g):
    for z in range(b):
      print(i,j,z,sep=' ')
print(r*g*b)
