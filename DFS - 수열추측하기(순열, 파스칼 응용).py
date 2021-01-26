import sys
sys.stdin = open("input.txt", "r")

def DFS(L, sum):
    if(L == N and sum == F):
        #N-1의 이항계수들을 구한다... 예를 들어 N=4 이면 1 3 3 1
        for x in res:
            print(x, end = " ")
        sys.exit(0)
    else:
        for i in range(1,N+1):
            if(ch[i] == 0):             
                ch[i] = 1
                res[L] = i
                DFS(L+1, sum + (bi[L]*res[L]))  
                ch[i] = 0
                
if __name__ == "__main__":
    N, F=map(int, input().split())
    ch = [0]*(N+1)
    res = [0]*N
    bi = [1]*(N)
    for i in range(1,N):
        temp = bi[i-1] * (N-i)
        temp = temp // i
        bi[i] = temp
    DFS(0, 0)

