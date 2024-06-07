import pygame
import config


def partition(to_sort, low, high):
    pygame.event.pump()
    pivot = to_sort.arr[high]
    i = low - 1

    for j in range(low, high):
        if to_sort.arr[j] <= pivot:
            i = i + 1
            pygame.time.delay(config.SORT_DELAY)

            to_sort.swap(i, j)

    to_sort.swap((i + 1), high)
    return i + 1


def quickSort(to_sort, low, high):
    if low < high:
        pi = partition(to_sort, low, high)

        quickSort(to_sort, low, pi - 1)

        quickSort(to_sort, pi + 1, high)
