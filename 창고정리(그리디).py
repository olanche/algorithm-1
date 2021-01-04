import sys
sys.stdin = open("input.txt", "r")
n = int( input())
a = list(  map(int, input().split()) )
m = int(input())
lar = 0
maxIndex = 0
small =0
minIndex = 0
for i in range(m):
    lar = max(a)
    small = min(a)
    maxIndex = a.index(max(a))
    minIndex = a.index(min(a))
    a[minIndex]+=1
    a[maxIndex]-=1

lar = max(a)
small = min(a)
print(lar - small)

    
'''
for i in range(n):
    print(a[i], end=" ")
'''
'''
list = [3,8,5,1,2,7,8,5]
print(list.index(max(list)))
'''
