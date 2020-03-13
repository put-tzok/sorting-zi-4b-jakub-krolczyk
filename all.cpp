#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

unsigned int ns[] = { 10, /* TODO: fill in "n" i.e. instance sizes */ };

void fill_increasing(int *t, unsigned int n) {
    int component = 10;
    for (int i=0; n > i; i++ )
    {
        t[i] = component;
        component++;
    }
}

void fill_decreasing(int *t, unsigned int n) {
    int component = 10;
    for(unsigned int i=0; n>i; i++)
    {
        t[i] = component;
        component--;
    }

}

void fill_vshape(int *t, unsigned int n) {

    int component = n;
    for(int i=0; n/2>i; i++)
    {
        t[i] = component;
        component = component - 2;
    }
    for(int i=(n/2); n>i; i++)
    {
        if(component == 1)
           {
               component--;
           }
        t[i] = component;
        component = component + 2;
    }
}

//Selection sort:

void selection_sort(int *t, unsigned int n) {
    // TODO: implement
}

//Insertion sort:

void insertion_sort(int *t, unsigned int n) {
    int key, i;
    n = n+1;
    for(unsigned int j=1; (n-1)>j; j++)
    {
        key = t[j];
        i = j- 1;

        while((i>=0)&&(t[i]>key))
        {
            t[i+1] = t[i];
            i--;

        }
        t[i+1] = key;
    }
}


//Quick sort:


int partition(int *A, int p, int r)
{
    int pivot = A[p];
    int i = p;
    int j = r;
    int w;

    while(1)
    {
        while(A[i] < pivot)
            i++;
        while(A[j] > pivot)
            j--;

    if(i < j)
    {
        w = A[i];
        A[i] = A[j];
        A[j] = w;
        i++;
        j--;
    }
        else
        return j;
    }
}

void quicksort(int *A, int p, int r)
{
    int q;

        if(p < r)
    {
        q = partition(A,p,r);
        quicksort(A, p, q);
        quicksort(A, q+1, r);
    }
}

void quick_sort(int *t,unsigned int n)
{
    quicksort(A, 0, n-1);
}



//Heap sort

void heap_sort(int *t, unsigned int n) {
    // TODO
}

void fill_random(int *t, unsigned int n) {
    for (unsigned int i = 0; i < n; i++) {
        t[i] = rand();
    }
}

void is_random(int *t, unsigned int n) {
    return;
}

void is_increasing(int *t, unsigned int n) {
    fill_increasing(t, n);
    for (unsigned int i = 1; i <= n; i++) {
        assert(t[i] > t[i - 1]);
    }
}

void is_decreasing(int *t,unsigned int n) {
    fill_decreasing(t, n);
    for (unsigned int i = 1; i < n; i++) {
        assert(t[i] < t[i - 1]);
    }
}

void is_vshape(int *t, unsigned int n) {
    fill_vshape(t, n);
    int *begin = t;
    int *end = t + n - 1;
    while (end - begin > 1) {
        assert(*begin > *end);
        begin++;
        assert(*end > *begin);
        end--;
    }
}

void is_sorted(int *t, unsigned int n) {
    for (unsigned int i = 1; i < n; i++) {
        assert(t[i] >= t[i - 1]);
    }
}

void (*fill_functions[])(int *, unsigned int) = { fill_random, fill_increasing, fill_decreasing, fill_vshape };
void (*check_functions[])(int *, unsigned int) = { is_random, is_increasing, is_decreasing, is_vshape };
void (*sort_functions[])(int *, unsigned int) = { selection_sort, insertion_sort, quick_sort, heap_sort };

char *fill_names[] = { "Random", "Increasing", "Decreasing", "V-Shape" };
char *sort_names[] = { "SelectionSort", "InsertionSort", "QuickSort", "HeapSort" };

int main() {
    for (unsigned int i = 0; i < sizeof(sort_functions) / sizeof(*sort_functions); i++) {
        void (*sort)(int *, unsigned int) = sort_functions[i];

        for (unsigned int j = 0; j < sizeof(fill_functions) / sizeof(*fill_functions); j++) {
            void (*fill)(int *, unsigned int) = fill_functions[j];
            void (*check)(int *, unsigned int) = check_functions[j];

            for (unsigned int k = 0; k < sizeof(ns) / sizeof(*ns); k++) {
                unsigned int n = ns[k];
                int *t = malloc(n * sizeof(*t));

                fill(t, n);
                check(t, n);

                clock_t begin = clock();
                sort(t, n);
                clock_t end = clock();
                is_sorted(t, n);

                printf("%s\t%s\t%u\t%f\n", sort_names[i], fill_names[j], n, (double)(end - begin) / (double) CLOCKS_PER_SEC);
                free(t);
            }
        }
    }
    return 0;
}
