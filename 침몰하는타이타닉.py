import sys
sys.stdin=open("input.txt", "r")
n, m = map(int, input().split())
p = list( map(int, input().split()))
p.sort()
cnt = 0
while( p ):
    if(len(p) == 1):
        cnt +=1
        break
    if(p[0] + p[-1] > m):
        p.pop()
        cnt +=1
    if(p[0]+p[-1]<=m):
        p.pop(0)
        p.pop()
        cnt +=1
   







print(cnt)

