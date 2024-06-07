import pygame
import config


def shellSort(toSort, n):
    arr = toSort.arr
    gap = n // 2

    while gap > 0:
        j = gap

        while j < n:
            i = j - gap

            while i >= 0:

                if arr[i + gap] > arr[i]:

                    break
                else:
                    pygame.time.delay(config.SORT_DELAY)
                    toSort.swap(i + gap, i)

                i = i - gap

            j += 1
        gap = gap // 2
