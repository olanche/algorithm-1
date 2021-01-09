import sys
sys.stdin = open( "input.txt", "r"   )
x = int(input())

a = []
def DFS(n):
    temp = n//2
    a.append(n%2) #나중에 리버스
    if(temp != 0):
        DFS(temp)
        



if __name__ == "__main__" :

    DFS(x)

    a.reverse() #이게 맞냐
    for i in a:
        print(i, end="")
