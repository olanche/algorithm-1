import sys
sys.stdin=open("input.txt", "rt")
n = int(input())
list = []
for i in range(n):
    s, e=map(int, input().split())
    list.append((s,e))
list.sort(reverse = True)
max = 0
cnt = 0
for x, y in list:
    if(max <= y):
        max = y
        cnt = cnt+1
print(cnt)
