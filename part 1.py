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

fill_decreasing(tablica, -100, 100)
print(tablica)
heap_sort(tablica)
print(tablica)
