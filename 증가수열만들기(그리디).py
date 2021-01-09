while(lt <= rt):
    if(a[lt] > last):
        temp.append((a[lt], "L"))
    if(a[rt] > last):
        temp.append((a[rt], "R"))
    if(a[lt] < last and a[rt] < last):
        break

    temp.sort()
    res+=temp[0][1]
    cnt +=1
    last = temp[0][0]
    if(temp[0][1] == "L"):
        lt +=1
    else:
        rt -=1
    temp.clear()
print(len(res))
print(res)
