def selection_sort(array):
    sorted_array = array[:]
    current_position = 0
    array_length = len(sorted_array)
    while current_position != array_length - 1:
        min_element_position = current_position
        for i in range(current_position, array_length-1):
            if sorted_array[min_element_position] > sorted_array[i+1]:
                min_element_position = i+1
        sorted_array[current_position], sorted_array[min_element_position] = \
            sorted_array[min_element_position], \
            sorted_array[current_position]
        current_position += 1
    return sorted_array
