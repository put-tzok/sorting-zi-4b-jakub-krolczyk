from random import randrange
from heapq import heappop, heappush
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
    for i in range(len(tablica)):
        min_idx = i
        for j in range(i+1, len(tablica)):
            if tablica[min_idx] > tablica[j]:
                min_idx = j


        tablica[i], tablica[min_idx] = tablica[min_idx], tablica[i]

def heap_sort(tablica):
    heap = []
    for i in tablica:
        heappush(heap, i)

    tablica.clear()

    while heap:
        tablica.append(heappop(heap))

    return tablica

def insertion_sort(tablica):
    for j in range(len(tablica)):
        key = tablica[j]
        i = j - 1

        while i >= 0 and tablica[i] > key:
            tablica[i + 1] = tablica[i]

            i = i - 1

        tablica[i + 1] = key
    return tablica

def partition(tablica, p, r):
    pivot = tablica[p]
    i = p + 1 #index mniejszy
    j = r #index większy

    while True:    #podział tablicy na dwie części:
        while i <= j and tablica[j] >= pivot:
            j = j - 1

        while i <= j and tablica[i] <= pivot:
            i = i + 1

        if i <= j:
            tablica[i], tablica[j] = tablica[j], tablica[i]
        else:
            break
    tablica[p], tablica[j] = tablica[j], tablica[p]

    return j

def quick_sort(tablica, p, r):
    if p >= r:
        return
    #rozdzielanie tablicy i ponownie poddawanie podzielonych części porządkowaniu:
    q = partition(tablica, p, r)
    quick_sort(tablica, p, q - 1)
    quick_sort(tablica, q + 1, r)

def quicksort(tablica):
    quick_sort(tablica, 0, len(tablica) - 1)
    return tablica


