"""
2). Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на промежутке [0; 50).
 Выведите на экран исходный и отсортированный массивы.
"""
import random

size = 10
array = [random.uniform(0, 50) for _ in range(size)]
random.shuffle(array)
print(array)


def mergeSort(theSeq):
    n = len(theSeq)
    tmpArray = [None for _ in range(n)]
    recMergeSort(theSeq, 0, n - 1, tmpArray)
    print(tmpArray)



def recMergeSort( theSeq, first, last, tmpArray ):
     if first == last:
         return;
     else:
         mid = (first + last) // 2
         recMergeSort(theSeq, first, mid, tmpArray)
         recMergeSort(theSeq, mid + 1, last, tmpArray)
     mergeVirtualSeq(theSeq, first, mid + 1, last + 1, tmpArray)


def mergeVirtualSeq(theSeq, left, right, end, tmpArray):
     a = left
     b = right
     m = 0
     while a < right and b < end:
         if theSeq[a] < theSeq[b]:
             tmpArray[m] = theSeq[a]
             a += 1
         else:
             tmpArray[m] = theSeq[b]
             b += 1
         m += 1
     while a < right:
         tmpArray[m] = theSeq[a]
         a += 1
         m += 1

     while b < end:
         tmpArray[m] = theSeq[b]
         b += 1
         m += 1

     for i in range(end - left):
         theSeq[i + left] = tmpArray[i]

mergeSort(array)