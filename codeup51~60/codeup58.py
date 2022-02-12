'''2개의 정수값이 입력될 때,
그 불 값(True/False) 이 모두 False 일 때에만 
True 를 출력하는 프로그램을 작성해보자.
'''
a,b =map(int,input().split())
print(bool(not(a or b)))


"""a, b = input().split()
c= bool(int(a))
d= bool(int(b)) 
print( not (c or d) )

출처: https://s0ng.tistory.com/entry/CodeUp-코드업-기초-100제-6058번-풀이-파이썬python [S0NG의 정보보안 블로그]
"""