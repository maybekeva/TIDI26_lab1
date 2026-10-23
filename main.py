import random
import matplotlib.pyplot as plt
import time
import csv
# ФУНКЦИИ........................................................................

# 1. ДВА УКАЗАТЕЛЯ

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


# 2. БИНАРНЫЙ ПОИСК
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


# 3. ЭКСПОНЕНЦИАЛЬНЫЙ ПОИСК
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




# 4. ДВОЙНОЙ БИНАРНЫЙ ПОИСК (с разделением)
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
    if (not a) or (not b):
        return False
    if len(a) <= len(b):
        return dual_search(a, b, 0, len(a) - 1, 0, len(b) - 1)
    else:
        return dual_search(b, a, 0, len(b) - 1, 0, len(a) - 1)


import csv
import time
import matplotlib.pyplot as plt


def get_arrays(N, m):
    big_arr = [x * 2 for x in range(N)]
    step = N // m
    small_arr = [i * step * 2 + 1 for i in range(m)]
    return big_arr, small_arr


def measure_time(func, a, b, repeats=10):
    p = []
    for _ in range(repeats):
        start = time.perf_counter()
        func(a, b)
        end = time.perf_counter()
        p.append((end - start))
    return sum(p) / len(p) * 1000


N = 10_000_000


sizes_M = [10, 100, 1_000, 10_000, 100_000, 1_000_000, 10_000_000]

funcs = [two_track, itog, exp_search, dual_binary]

times_two_track = []
times_itog = []
times_exp = []
times_dual = []



for m in sizes_M:
    ar1, ar2 = get_arrays(N, m)

    t1 = measure_time(two_track, ar1, ar2)
    times_two_track.append(t1)

    t2 = measure_time(itog, ar1, ar2)
    times_itog.append(t2)

    t3 = measure_time(exp_search, ar1, ar2)
    times_exp.append(t3)

    t4 = measure_time(dual_binary, ar1, ar2)
    times_dual.append(t4)

    print(f"Размер M = {m} успешно посчитан!")


with open("raw_data.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f, delimiter=";")
    writer.writerow(
        ["M", "Two_Pointers", "Binary_Search", "Exponential", "Dual_Binary"]
    )
    for i in range(len(sizes_M)):
        writer.writerow(
            [
                sizes_M[i],
                times_two_track[i],
                times_itog[i],
                times_exp[i],
                times_dual[i],
            ]
        )

plt.figure(figsize=(10, 6))
plt.plot(sizes_M, times_two_track, marker="o", label="Два указателя O(M+N)")
plt.plot(sizes_M, times_itog, marker="s", label="Бинарный O(M log N)")
plt.plot(
    sizes_M, times_exp, marker="^", label="Экспоненциальный O(M log(N/M))"
)
plt.plot(sizes_M, times_dual, marker="d", label="Двойной бинарный O(M log(N/M))")

plt.xscale("log")
plt.yscale("log")

plt.xlabel("Длина меньшего массива M (лог. шкала)")
plt.ylabel("Время выполнения, мс (лог. шкала)")
plt.title(f"Сравнение алгоритмов при фиксированном N = {N} (Худший случай)")
plt.grid(True, which="both", ls="--", alpha=0.5)
plt.legend()
plt.tight_layout()

plt.savefig("plot_results.png", dpi=300)
plt.close()