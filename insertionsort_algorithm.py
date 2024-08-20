import pygame
import config


def insertionSort(toSort, n):
    arr = toSort.arr

    if n <= 1:
        return

    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            pygame.time.delay(config.SORT_DELAY)
            toSort.insert(j + 1, arr[j])
            j -= 1
        toSort.insert(j + 1, key)
