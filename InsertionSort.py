def insertion_sort(array):
    sorted_array = array[:]
    array_length = len(array)
    for i in range(1, array_length):
        new_position = i
        current_element = sorted_array[i]
        for j in reversed(range(i)):
            if current_element < sorted_array[j]:
                new_position = j
        if new_position != i:
            del sorted_array[i]
            sorted_array.insert(new_position, current_element)
    return sorted_array
