import sys
sys.stdin = open("input.txt", "r")

def DFS(x,l=[]): #는 계층의 레벨을 의미한다 (0부터 시작합니다..)
    if( x == m):
        global cnt
        for j in range(m):
            print(a[j], end=" ")
        print()
        cnt+=1
    else:
        for i in range(1,n+1):
            if(isList[i] == 0):
                isList[i]=1
                a[x] = i
                DFS(x+1)
                isList[i]=0
            else:
                continue
        


if __name__ == "__main__" :
    n, m=map(int, input().split())
    cnt = 0
    a =[0]*n
    isList = [0]*(n+1)
    DFS(0)
    print(cnt)
