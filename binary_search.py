a = list(map(int, input().split()))
b = list(map(int, input().split()))


def bin_secc(h,k):
    l = 0
    r = len(h)-1
    while l<=r:
        m = (l+r)//2
        if h[m] == k: return True
        elif h[m] < k:
            l = m + 1
        else:
            r = m -1
    return False

def itog(a,b):
    n = len(a)
    m = len(b)
    if n < m:
        for el in a:
            if bin_secc(b,el): return True
    else:
        for el in b:
            if bin_secc(a,el): return True
    return False

print(itog(a,b))











































































































