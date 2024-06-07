import pygame
import insertionsort_algorithm
import quicksort_algorithm
import bubblesort_algorithm
import config
import shellsort_algorithm
import visuals
import threading


pygame.display.set_caption("Sorting Algorithm")
screen = pygame.display.set_mode((config.COLUMNS * config.SIZEMULT, config.HEIGHT * config.SIZEMULT))
clock = pygame.time.Clock()
to_sort_array = visuals.ToSort(config.COLUMNS, config.RANDOM_CAP)
display = visuals.Display(to_sort_array, screen)
sorting_choice = 1
sorting_thread = threading.Thread

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:

            # Left click starts the sorting algorithm.
            if event.button == 1:
                if threading.active_count() < 2:

                    if sorting_choice == 1:
                        sorting_thread = threading.Thread(target=quicksort_algorithm.quickSort,
                                                          args=(to_sort_array, 0, to_sort_array.arr.size - 1))

                    elif sorting_choice == 2:
                        sorting_thread = threading.Thread(target=bubblesort_algorithm.bubbleSort,
                                                          args=(to_sort_array,to_sort_array.arr.size))
                        # bubblesort_algorithm.bubbleSort(to_sort_array)

                    elif sorting_choice == 3:
                        sorting_thread = threading.Thread(target=insertionsort_algorithm.insertionSort,
                                                          args=(to_sort_array,to_sort_array.arr.size))

                    elif sorting_choice == 4:
                        sorting_thread = threading.Thread(target=shellsort_algorithm.shellSort,
                                                          args=(to_sort_array, to_sort_array.arr.size))

                    sorting_thread.start()

            # Right click resets the array.
            elif event.button == 3:
                to_sort_array.recreate_array()

            # Mouse wheel up changes the sort used.
            elif event.button == 4:
                if sorting_choice - 1 != 0:
                    sorting_choice -= 1
                else:
                    sorting_choice = 4

                if sorting_choice == 1:
                    print("quick sort")
                elif sorting_choice == 2:
                    print("bubble sort")
                elif sorting_choice == 3:
                    print("insert sort")
                elif sorting_choice == 4:
                    print("shell sort")
            # Mouse wheel down changes the sort used.
            elif event.button == 5:
                if sorting_choice + 1 > 4:
                    sorting_choice = 1
                else:
                    sorting_choice += 1

                if sorting_choice == 1:
                    print("quick sort")
                elif sorting_choice == 2:
                    print("bubble sort")
                elif sorting_choice == 3:
                    print("insert sort")
                elif sorting_choice == 4:
                    print("shell sort")


    display.clear_screen()
    display.update_screen()
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
