def bubble_sort(array):
    is_swap = True
    sorted_array = array[:]
    array_length = len(sorted_array)
    while is_swap:
        is_swap = False
        for i in range(0, array_length):
            is_should_swap = i+1 != array_length and sorted_array[i] > sorted_array[i+1]
            if is_should_swap:
                sorted_array[i], sorted_array[i+1] = sorted_array[i+1], sorted_array[i]
                is_swap = True
    return sorted_array
