import sys
sys.stdin= open("input.txt", "r")
n = int(input())
a = list( map (int, input().split()))
b = [None]*n

temp = a[0]
b[temp] = 1

for i in range(1,n):
    cnt = 0

    for j in range(n):
        if(cnt == a[i]):
            b[cnt + i] = i+1
            break
            
            
        if b[j]:
            continue
        else:
            cnt +=1
            
        
