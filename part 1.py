from random import randrange
from heapq import heappop, heappush
import time
tablica = []
def fill_increasing(tablica, n, m):
    for i in range(n, m):
        tablica.append(i)

def fill_decreasing(tablica, n, m):
    for i in range(n, m):
        tablica.append(i)
    tablica.reverse()

def fill_random(tablica, n, m):
    for i in range(n, m):
        k = randrange(n, m)
        tablica.append(k)
        
def fill_vshape(tablica, n, m):
    tablica1 = []
    for i in range(n, m):
        k = randrange(n, m)
        tablica1.append(k)
    tablica1.sort()
    tablica1.reverse()
    tab1 = tablica1[::2]
    print(tab1)
    tab2 = tablica1[1::2]
    print(tab2)
    tab2.sort()
    print(tab2)
    tablica.extend(tab1)
    tablica.extend(tab2)

def is_increasing(tablica):
    for i in range(len(tablica) - 1):
        assert tablica[i] < tablica[i+1]

def is_decreasing(tablica):
    for i in range(len(tablica) - 1):
        assert tablica[i] > tablica[i+1]

def selection_sort(tablica):
    start = time.time()
    tablica1 = tablica[:]
    for i in range(len(tablica1)):
        min_idx = i
        for j in range(i+1, len(tablica1)):
            if tablica1[min_idx] > tablica1[j]:
                min_idx = j


        tablica1[i], tablica1[min_idx] = tablica1[min_idx], tablica1[i]
    end = time.time()
    finish = (end - start)
    return finish

def heap_sort(tablica):
    start = time.time()
    tablica1 = tablica[:]
    heap = []
    for i in tablica1:
        heappush(heap, i)

    tablica1.clear()

    while heap:
        tablica1.append(heappop(heap))

    end = time.time()
    finish = (end - start)
    return finish

def insertion_sort(tablica):
    start = time.time()
    tablica1 = tablica[:]
    for j in range(len(tablica1)):
        key = tablica1[j]
        i = j - 1

        while i >= 0 and tablica1[i] > key:
            tablica1[i + 1] = tablica1[i]

            i = i - 1

        tablica1[i + 1] = key
    end = time.time()
    finish = (end - start)
    return finish

def partition(tablica, p, r):
    tablica1 = tablica[:]
    pivot = tablica1[p]
    i = p + 1 #index mniejszy
    j = r #index większy

    while True:    #podział tablicy na dwie części:
        while i <= j and tablica1[j] >= pivot:
            j = j - 1

        while i <= j and tablica1[i] <= pivot:
            i = i + 1

        if i <= j:
            tablica1[i], tablica1[j] = tablica1[j], tablica1[i]
        else:
            break
    tablica1[p], tablica1[j] = tablica1[j], tablica1[p]

    return j

def quick_sort(tablica, p, r):
    tablica1 = tablica[:]
    if p >= r:
        return
    #rozdzielanie tablicy i ponownie poddawanie podzielonych części porządkowaniu:
    q = partition(tablica1, p, r)
    quick_sort(tablica1, p, q - 1)
    quick_sort(tablica1, q + 1, r)

def quicksort(tablica):
    start = time.time()
    tablica1 = tablica[:]
    quick_sort(tablica1, 0, len(tablica1) - 1)
    end = time.time()
    finish = (end - start)
    return finish
