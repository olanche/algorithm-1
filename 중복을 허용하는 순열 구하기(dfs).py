import sys
sys.stdin = open( "input.txt", "r")


def DFS(L):
    global cnt
    if( L == m ):
        for j in range(m):
            print(a[j], end=" ")
        print()
        cnt = cnt+1
            
    else:
        for i in range(n):
            a[L] = i+1
            DFS(L+1)
        



if __name__ == "__main__":

    n,m = map(int, input().split() )
    a = [0]*n
    cnt = 0
    DFS(0)
    print(cnt)
