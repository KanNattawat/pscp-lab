'''Boomerang'''
import math
def main():
    '''Boomerang'''
    num_x = int(input())
    num_y = int(input())
    num_z = int(input())
    root = math.sqrt((num_y ** 2) - (4 * num_x * num_z))
    print(num_x + 1)
    print((7 * (num_y ** 3)) + (2 * (num_y ** 2)) - (31 * num_y) + 1)
    print(num_z * -1)
    print((num_x + num_y) * (num_x - num_y))
    print((num_y - root) / (2 * num_x))
main()
