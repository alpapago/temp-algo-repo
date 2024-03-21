import sys
input = sys.stdin.readline

n,m,l,k = map(int,input().split())
stars = []

# 별의 값 입력받기
for _ in range(k):
    x,y = map(int,input().split())
    