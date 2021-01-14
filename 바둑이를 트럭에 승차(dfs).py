import sys
sys.stdin = open("input.txt", "r")


def DFS (x) :
    if(  x == n      ):
        sumList.append(sum(temp))


    else:
        temp[x] = a[x]
        DFS(x+1)
        temp[x]=0
        DFS(x+1)
        



if __name__ == "__main__" :
    c, n = map(  int,  input().split()           ) #띄어쓰기로 두개 받고 int로 바꾸기
    a=[]
    for i in range(n):
        a.append(   int(input())    )
        

    '''a = list(      map(  int,  input().split()           )    )'''#받는 리스트

    sumList = []
    temp = [0] * (n+1)

    DFS(0)
    temp2 = 0

    for i in sumList:
        if (i>c):
            sumList.pop(temp2)
            temp2 +=1
    print(max(sumList))
