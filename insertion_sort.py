def insertion_sort(arr):
    for idx in range(len(arr)+1):
        key_element = arr[idx]

        jdx = idx - 1

        while jdx >= 0 and key < arr[jdx]:
            arr[jdx + 1] = arr[jdx]
            jdx = jdx - 1
        arr[jdx] = key_element

