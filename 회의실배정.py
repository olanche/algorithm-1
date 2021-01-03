import sys
sys.stdin=open("input.txt", "r")
n=int(input())
list = []
for i in range(n):
    s, e=map(int, input().split())
    list.append((s,e))
list.sort(key = lambda x : (x[1], x[0]))
cnt = 0
et = 0
for s,e in list:
    if(s >= et):
        cnt = cnt+1
        et = e
print(cnt)
