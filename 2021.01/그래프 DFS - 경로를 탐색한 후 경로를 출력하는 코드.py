import sys
sys.stdin = open("input.txt", "r")

def DFS(L):
    global cnt
    if(L == N):
        for j in path:
            print(j, end = " ")
        print()

    else:
        for i in range(1, N+1):
            if(g[L][i] == 1 and ch[i] == 0):
                ch[i] = 1 #체크리스트 만들어서 이미 간곳을 다시 갈수 없게 해야한다
                path.append(i)
                DFS(i)
                ch[i] = 0
                path.pop()
'''깊이 우선 탐색을 끝까지 실행한 후 뻗었던 가지의 뒤로 되돌아올때는 ch  리스트의 값
을 반드시 1에서 0ㅇ로 풀어주어야 한다''' 


if __name__ == "__main__":
    N, M = map(int, input().split())
    g = [[0]*(N+1) for _ in range(N+1)]
    for i in range(M):
        a,b = map(int, input().split())
        g[a][b] = 1
    ch = [0]*(N+1)
    cnt = 0
    ch[1] = 1
    path = [] #경로의 노드를 저장하기 위한 리스트
    path.append(1)
    DFS(1)
    

