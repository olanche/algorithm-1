import sys
sys.stdin = open("input.txt", "r")
n, m=map(int, input().split()) #n은 노드의 갯수, m은 간선의 갯수

g=[[0]*(n+1) for _ in range(n+1)]

for i in range(m) :
    a, b, c=map(int, input().split())
    g[a][b] = c

for i in range(1, n+1):
    for j in range(1, n+1):
        print(g[i][j], end=' ')
    print()

#주의할 점 => 항상 '행'에서 '열'로 이동한다
