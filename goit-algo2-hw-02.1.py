import time
import random

def find_min_max(arr, left, right):
    if left == right:
        return arr[left], arr[left]

    mid = (left + right) // 2

#Використано рекурсивний підхід (10 б).
    left_min, left_max = find_min_max(arr, left, mid)
    right_min, right_max = find_min_max(arr, mid + 1, right)

    if left_min < right_min:
        overall_min = left_min
    else:
        overall_min = right_min

    if left_max > right_max:
        overall_max = left_max
    else:
        overall_max = right_max

#Повертається кортеж значень (мінімум, максимум) (10 б).
    return overall_min, overall_max


#Функція приймає масив чисел довільної довжини (10 б).
arr = [21, -4, 1, 91, -60, 7, -3, 52, -8, 44, 0, -2, 6, -1, 3, -7, 8, -54, 19, -9]
minimum, maximum = find_min_max(arr, 0, len(arr) - 1)

print(f"Мінімальний елемент: {minimum}")
print(f"Максимальний елемент: {maximum}")


# Перевірка часу виконання для підтвердження складністі алгоритму — O(n) (10 б).
sizes = [1000, 5000, 10000, 20000, 40000]
for n in sizes:
    arr = [random.randint(-1000, 1000) for _ in range(n)]
    start_time = time.time()
    find_min_max(arr, 0, len(arr) - 1)
    end_time = time.time()
    elapsed = end_time - start_time
    print(f"n={n}, час виконання ≈ {elapsed:.6f} секунд")
