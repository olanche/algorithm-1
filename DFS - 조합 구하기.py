import sys
sys.stdin=open("input.txt", "r")

def DFS(L,s):
    global cnt
    if L == M :
        for j in range(0,M):
            print(res[j], end=" ")

        print()
        cnt = cnt+1
        
    else:
        for i in range(s, N+1):
            res[L] = i
            DFS(L+1, i+1)


if __name__ == "__main__":
    N, M = map(int, input().split())
    cnt = 0
    res = [0]*(M)
    DFS(0,1)
    print(cnt)
