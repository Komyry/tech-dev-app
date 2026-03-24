import random
import time

# База данных из 5000 сотрудников
employees = []
for i in range(1, 5001):
    employees.append({
        'tab_num': i,
        'FIO': f'Фамилия{i} Имя{i} Отчество{i}',
        'position': 'Должность' + str(i % 10),
        'department': 'Отдел' + str(i % 5)
    })

# Ввод искомого табельного номера
target = int(input("Введите табельный номер для поиска: "))

# 1. Линейный поиск
start_time = time.time()
linear_result = None
for emp in employees:
    if emp['tab_num'] == target:
        linear_result = emp
        break
linear_time = time.time() - start_time

employees_sorted = sorted(employees, key=lambda x: x['tab_num'])

# 2. Бинарный поиск
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid]['tab_num'] == target:
            return arr[mid]
        elif arr[mid]['tab_num'] < target:
            left = mid + 1
        else:
            right = mid - 1
    return None

start_time = time.time()
binary_result = binary_search(employees_sorted, target)
binary_time = time.time() - start_time

# 3. Поиск прыжками
import math

def jump_search(arr, target):
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0
    while prev < n and arr[min(step, n)-1]['tab_num'] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return None
    for i in range(prev, min(step, n)):
        if arr[i]['tab_num'] == target:
            return arr[i]
    return None

start_time = time.time()
jump_result = jump_search(employees_sorted, target)
jump_time = time.time() - start_time

# Вывод результатов
print("\nРезультаты поиска:")
if linear_result:
    print("Линейный поиск: найден", linear_result)
else:
    print("Линейный поиск: сотрудник не найден")

if binary_result:
    print("Бинарный поиск: найден", binary_result)
else:
    print("Бинарный поиск: сотрудник не найден")

if jump_result:
    print("Поиск прыжками: найден", jump_result)
else:
    print("Поиск прыжками: сотрудник не найден")

# Таблица сравнения времени
print("\nСравнение времени работы алгоритмов (в секундах):")
print(f"{'Алгоритм':<20} {'Время (с)':<15}")
print(f"{'Линейный':<20} {linear_time:.6f}")
print(f"{'Бинарный':<20} {binary_time:.6f}")
print(f"{'Прыжками':<20} {jump_time:.6f}")