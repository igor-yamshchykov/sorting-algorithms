from BubbleSort import bubble_sort
from InsertionSort import insertion_sort
from SelectionSort import selection_sort

def get_user_input():
    while True:
        user_input = input('Please enter array values comma separated \n')
        try:
            return list(map(int, user_input.split(',')))
        except ValueError:
            print('Invalid input, enter comma separated numbers')

if __name__ == '__main__':
    array = get_user_input()
    print('Sorted array with bubble sort {0}'.format(bubble_sort(array)))
    print('Sorted array with insertion sort {0}'.format(insertion_sort(array)))
    print('Sorted array with selection sort {0}'.format(selection_sort(array)))
