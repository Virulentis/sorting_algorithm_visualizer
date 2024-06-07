import pygame
import config


def bubbleSort(to_sort, n):
    arr = to_sort.arr


    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            pygame.event.pump()

            if arr[j] > arr[j + 1]:
                pygame.time.delay(config.SORT_DELAY)
                to_sort.swap(j, j + 1)

                swapped = True

        if not swapped:
            break
