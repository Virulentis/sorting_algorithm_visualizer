import numpy as np
import pygame
import config



class ToSort:

    def __init__(self, column, random_cap):
        self.arr = np.random.randint(random_cap, size=column)
        self.cols = column
        self.randCap = random_cap
        self.red_list = set()

    def recreate_array(self):
        self.arr = np.random.randint(self.randCap, size=self.cols)

    def swap(self, swap_a, swap_b):
        self.arr[swap_a], self.arr[swap_b] = self.arr[swap_b], self.arr[swap_a]
        self.red_list.add(swap_b)
        self.red_list.add(swap_a)

    def insert(self, position, insert_value):
        self.arr[position] = insert_value
        self.red_list.add(position)

class Display:

    def __init__(self, to_sort, screen):
        self.screen = screen
        self.to_sort = to_sort

    def clear_screen(self):
        self.screen.fill("black")

    def update_screen(self):
        for x, element in enumerate(self.to_sort.arr):
            rectangle = (x * config.SIZEMULT, element * config.SIZEMULT, config.SIZEMULT, 9999)

            if x in self.to_sort.red_list:
                self.to_sort.red_list.discard(x)
                color = "red"

            else:
                color = "white"

            pygame.draw.rect(self.screen, color, rectangle)
            pygame.draw.rect(self.screen, "black", rectangle, 1, border_radius=1)
