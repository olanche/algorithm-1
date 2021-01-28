import sys
sys.stdin = open("input.txt", "r")

def DFS(L, s, su):
    global cnt
    if L == K:
        if su % 6 == 0 :
            cnt +=1
    else:
        for i in range( s, N    ):
            DFS(L+1, i+1, su + a[i])


if __name__ == "__main__":
    N, K=map(int, input().split())
    a = list(map(int, input().split()))
    M = input()
    #res = [0]*K
    cnt = 0
    DFS(0,0,0)
    print(cnt)
