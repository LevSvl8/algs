# coding=utf-8

def summa(arr):
    if arr == []:
        return 0
    else:
        return arr[-1]+summa(arr[0:-1])

def count_elements(arr):
    if arr == []:
        return 0
    else:
        return 1 + count_elements(arr[0:-1])

def find_max_element(arr):
    if arr == []:
        return 0
    else:
        return arr[-1] if arr[-1]>find_max_element(arr[0:-1]) else find_max_element(arr[0:-1])

def binary_search(arr,item):
    low = 0
    high = len(arr) - 1
    while low <=high:
        mid = (low+high)/2
        guess = arr[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
        binary_search(arr[low:high],item)

def qsort1(arr):
    if arr.__len__() < 2:
        return arr
    else:
        less = []
        more = []
        mid = len(arr)/2
        for el in arr:
            if el < arr[mid]:
                less.append(el)
            elif el > arr[mid]:
                more.append(el)
        return qsort1(less) + [arr[mid]] + qsort1(more)

def qsort2(arr):
    if arr.__len__() < 2:
        return arr
    else:
        mid = len(arr)/2
        less = [el for el in arr if el<arr[mid]]
        more = [el for el in arr if el>arr[mid]]
        return qsort2(less) + [arr[mid]] + qsort2(more)
# сортировка слиянием из интернета
def merge_sort(arr):
    if arr.__len__() > 1:
        mid = arr.__len__() / 2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                arr[k] = left[i]
                i+=1
            else:
                arr[k] = right[j]
                j+=1
            k+=1

        while j < len(right):
            arr[k] = right[j]
            j+=1
            k+=1
        while i < len(left):
            arr[k] = left[i]
            i+=1
            k+=1
        return arr


def fact_seq(n):
    if n == 1:
        return 1
    else:
        return n + fact_seq(n-1)

def find_2_from_3(low,high):
    kr3 = []
    i = low
    while i <= high:
        if i % 3 == 2:
            kr3.append(i)
        i+=1
    return kr3

def two_from_mod(low,high):
    if high <= 3:
        return []
    else:
        return ([high] if high % 3==2 else []) + two_from_mod(low,high-1)


if __name__ == '__main__':
    print two_from_mod(3,12)
    print find_2_from_3(2,12)