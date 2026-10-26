
def exp_search(a,b):
    l1 = 0
    n = len(a)

    l2 = 0
    m = len(b)

    prev1 = 0
    prev2 = 0



    while l1 < n and l2 < m:
        shag = 1
        if a[l1] == b[l2]: return True
        elif a[l1] < b[l2]:
            while a[l1] < b[l2]:

                if shag+l1>n-1:
                    prev1 = l1
                    l1 = n-1
                    break
                else:
                    prev1 = l1
                    l1 = l1 + shag
                shag*=2

            left = prev1
            right = l1

            while left <= right:
                mid = (left + right) // 2
                if a[mid] == b[l2]:
                    return True
                elif a[mid] < b[l2]:
                    left = mid + 1
                else:
                    right = mid - 1
            l1 = left
            l2+=1


        else:
            while a[l1] > b[l2]:

                if shag + l2 > m - 1:
                    prev2 = l2
                    l2 = m - 1
                    break
                else:
                    prev2 = l2
                    l2 = l2 + shag
                shag *= 2

            left = prev2
            right = l2
            while left <= right:
                mid = (left + right) // 2
                if a[l1] == b[mid]:
                    return True
                elif b[mid] < a[l1]:
                    left = mid + 1
                else:
                    right = mid - 1
            l2 = left
            l1 += 1
    return False
