

def two_track(a,b):
    l1 = 0
    n = len(a)

    l2 = 0
    m = len(b)


    while l1 < n and l2 < m:
        if a[l1] == b[l2]: return True
        elif a[l1] > b[l2]:
            l2+=1
        else:
            l1+=1
    return False


