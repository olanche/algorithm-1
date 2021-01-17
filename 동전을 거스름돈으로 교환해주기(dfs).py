import sys
sys.stdin = open("input.txt", "r")

def DFS(x, sum):
    global minNum
    if( x+1 >= minNum ): #가지치기 - 더이상 탐색을 할 필요가 없음
        return
    if(sum > m):
        return 
        
    if(sum == m):
        if(   minNum>n):
            minNum =n 
        

    else:
        for i in range(0, n):
            DFS(x+1 ,sum + a[i] )
        




if __name__ == "__main__":
    n = int(  input())
    a = list( map(int,input().split() )   )
    a.sort(reverse = True)#복잡도를 줄이기위해서
    m = int(  input())
    cnt = 0
    minNum = 2147000000

    DFS(0, 0)
    print(minNum)
