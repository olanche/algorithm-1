import sys
sys.stdin = open("input.txt", "r")

def DFS(L, sum):
    if(  L == n  ):
        if( sum == (total - sum)   ):
            print("YES")
            sys.exit(0) #함수가 종료되는게 아니라 프로그램 전체를 종료시킨다
        
    else:
        
        DFS(L+1, sum+a[L])
        
        DFS(L+1, sum)
        




if __name__ == "__main__":
    n = int(  input())
    a = list  (       map(int, input().split())     )
    total = sum(a)
    DFS(  0 ,0   )
    print("NO")

    
