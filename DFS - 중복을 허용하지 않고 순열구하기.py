import sys
sys.stdin = open("input.txt", "r")

def DFS(x): #는 계층의 레벨을 의미한다 (0부터 시작합니다..)
    if( x == m):
        print( a )
        
    else:
        for i in range(1,n+1):
            if (i in isList):
                continue
            else:
                DFS(i)
                isList.append(i)



if __name__ == "__main__" :
    n, m=map(int, input().split())
    a =[]
    isList = []

