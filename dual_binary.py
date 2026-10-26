
def mesto_search(arr, h, l, r):
    while l<=r:
        mid = (l+r)//2
        if arr[mid] == h:
            return mid
        elif arr[mid] >h:
            r = mid -1
        else:
            l = mid+1
    return l


def dual_search(a,b, al,ar,bl,br):
    if al > ar or bl > br:
        return False
    middle = (al+ar)//2

    mesto = mesto_search(b,a[middle], bl, br)

    if mesto <= br and b[mesto] == a[middle]: return True



    if dual_search(a,b,al,middle-1, bl,mesto-1):
        return True
    if dual_search(a,b, middle+1,ar,mesto,br):
        return True
    return False

def dual_binary(a,b):
    if (not a) and (not b):
        return False
    if len(a) <= len(b):
        return dual_search(a, b, 0, len(a) - 1, 0, len(b) - 1)
    else:
        return dual_search(b, a, 0, len(b) - 1, 0, len(a) - 1)


