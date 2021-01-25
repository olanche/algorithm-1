import sys
sys.stdin = open("input.txt", "r")

def DFS(L):
    if(L == N):
        for i in range(N-1, 0, -1):
            for j in range(0,i):
                res[j] = res[j]+res[j+1]
        if(res[0] == F):
            print(res[0])
            #프로그램 자체를 종료한다
    else:
        for i in range(1,N+1):
            if(ch[i] == 1):
                continue
            else:                
                ch[i] = 1
                res.append(i)
                DFS(L+1)  
                ch[i] = 0
                res.pop()
                
if __name__ == "__main__":
    N, F=map(int, input().split())
    ch = [0]*(N+1)
    res = []
    DFS(0)
