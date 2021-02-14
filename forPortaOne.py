#!/usr/bin/python
# This Python file uses the following encoding: utf-8
import time
start_time = time.time()
def is_number(num):
    try:
        int(num)
        return True
    except ValueError:
        return False
        
with open('10m_2021.txt') as file:
    nums = file.read().splitlines()
    data = []
    for i in nums:
        data.append(int(i)) if is_number(i) else print('невалидные данные --> ', i)

sorted_list = sorted(data)

print('maximum number: ',sorted_list[-1])
print('minimum number: ',sorted_list[0])

def average(arr):
    list_length = len(arr)
    amount = 0
    for i in arr:
        amount += i
    return amount / list_length 

def mediana(arr):
    idx = len(arr) // 2
    if (len(arr) % 2 == 1):
        return arr[idx]
    else:
        return (arr[idx] + arr[idx - 1]) / 2

def max_sequence(data):
    arr = [[data[0]]]
    for i in range(1, len(data)):
        if data[i - 1] >= data[i]:arr.append([])
        arr[-1].append(data[i])
    return (max(arr, key = len))

def min_sequence(data):
    arr = [[data[0]]]
    for i in range(1, len(data)):
        if data[i - 1] <= data[i]:arr.append([]) 
        arr[-1].append(data[i])
    return (max(arr, key = len))



print('average: ', average(data))
print('median: ', mediana(sorted_list))
print('max_sequence: ', max_sequence(data))
print('min_sequence: ', min_sequence(data))

print("--- %s seconds ---" % (time.time() - start_time))
