no_list = [22,22,2,1,11,11,2,2,3,3,3,4,5,5,5,55,55,66]

def unique_list(l):
    for i in range(0,len(l),1):
        try:
            for j in range (i,len(l),1):
                if l[int(j)] == l[int(i)]:
                    del l[j]
        except:
            if(1==1):
                continue
    return l
print(unique_list(no_list))