import sys
sys.stdin = open("input.txt", "r")
n = int(input())
a = list( map(int, input().split()   )  )

b = [None]*n #출력할 리스트

temp = a[0]
b[temp] = 1

for i in range (1, n):
    cnt = 0
    for j in range(n):
        if(cnt == a[i]):
            b[j] = i+1
            break

        if b[j]:
            if(i+1 > b[j]):
                continue
        else:
            cnt +=1




        '''
        if( i+1 > b[j]):
            continue
        else:
            if(cnt == a[i]):
                break
            cnt += 1
        '''
    
