import random
import csv
import time
import matplotlib.pyplot as plt

from binary_search import itog
from dual_binary import dual_binary
from exp_search import exp_search
from two_trackers import two_track


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
