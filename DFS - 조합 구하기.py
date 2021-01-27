import sys
sys.stdin=open("input.txt", "r")

def DFS(L):
    if L == M :
        temp = set(res)
        if (temp in f):
            return
        else:
            f.append(temp)
            print(temp)
        
        
    else:
        for i in range(1, N+1):
            if ch[i] == 0 :
                ch[i] = 1
                res[L] = i
                DFS(L+1)
                ch[i] = 0


if __name__ == "__main__":
    N, M = map(int, input().split())
    ch = [0]*(N+1)
    res = [0]*(N+1)
    f = []
    DFS(0)
