import random
import time
import matplotlib.pyplot as plt


def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2


        if arr[mid] == target:
            return mid


        elif arr[mid] < target:
            left = mid + 1


        else:
            right = mid - 1


    return -1

list_size = 100
random_list = [random.randint(0, 1000) for _ in range(list_size)]

sorted_list = sorted(random_list)


target1 = sorted_list[random.randint(0, list_size - 1)]
target2 = 9999
target3 = sorted_list[0]
target4 = sorted_list[-1]


def linear_search(arr, target):

    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


def measure_time(search_func, arr, target):

    start_time = time.perf_counter()
    search_func(arr, target)
    end_time = time.perf_counter()
    return (end_time - start_time) * 1000



list_sizes = [100, 1000, 10000, 100000, 1000000]
binary_times = []
linear_times = []

for size in list_sizes:
    arr = sorted([random.randint(0, size) for _ in range(size)])

    target = arr[-1]

    binary_times.append(measure_time(binary_search, arr, target))
    linear_times.append(measure_time(linear_search, arr, target))


plt.figure(figsize=(10, 6))
plt.plot(list_sizes, binary_times, label='Бинарный поиск', marker='o')
plt.plot(list_sizes, linear_times, label='Линейный поиск', marker='x')
plt.xlabel('Размер списка (N)')
plt.ylabel('Время выполнения (мс)')
plt.title('Сравнение времени выполнения бинарного и линейного поиска')
plt.legend()
plt.grid(True)
plt.xscale('log')
plt.yscale('log')
plt.show()