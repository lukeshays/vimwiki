def bubblesort(array):
    n = len(array)
    for x in range(n):
        for y in range(n-1):
            if array[y] > array[y+1]:
                array[y], array[y+1] = array[y+1], array[y]
    return array

def bubblesort_optimized(array):
    n = len(array)
    for x in range(n):
        for y in range(n-1-x):
            if array[y] > array[y+1]:
                array[y], array[y+1] = array[y+1], array[y]
    return array

if __name__ == "__main__":
    test_arrays = [
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [1, 2, 5, 4, 3],
        [1, 1, 1, 1, 1],
        [],
    ]

    for array in test_arrays:
        print(f"Input: {array}")
        output = bubblesort(array)
        output_optimized = bubblesort_optimized(array)
        print(f"Output: {output}")
        print(f"Output Optimized: {output_optimized}\n")
