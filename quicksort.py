# Python3 implementation of QuickSort

# This Function handles sorting part of quick sort
# start and end points to first and last element of
# an array respectively


def partition(start, end, array_):
    # Initializing pivot's index to start
    pivot_index = start
    pivot = array[pivot_index]

    # This loop runs till start pointer crosses
    # end pointer, and when it does we swap the
    # pivot with element on end pointer
    while start < end:
        # Increment the start pointer till it finds an
        # element greater than  pivot
        while start < len(array_) and array_[start] <= pivot:
            start += 1

        # Decrement the end pointer till it finds an
        # element less than pivot
        while array_[end] > pivot:
            end -= 1

        # If start and end have not crossed each other,
        # swap the numbers on start and end
        if (start < end):
            array_[start], array_[end] = array_[end], array_[start]

    # Swap pivot element with element on end pointer.
    # This puts pivot on its correct sorted place.
    print(f"Swapping {array_[end]}, {array_[pivot_index]}")
    array_[end], array_[pivot_index] = array_[pivot_index], array_[end]
    print(f"To {array_[end]}, {array_[pivot_index]}, split pointer {end}")

    # Returning end pointer to divide the array into 2
    return end


# The main function that implements QuickSort
def quick_sort(start, end, array):
    if (start < end):
        # p is partitioning index, array[p]
        # is at right place
        p = partition(start, end, array)

        # Sort elements before partition
        # and after partition
        quick_sort(start, p - 1, array)
        quick_sort(p + 1, end, array)


if __name__ == "__main__":
    # Driver code
    array = [10, 7, 8, 9, 1, 5]
    quick_sort(0, len(array) - 1, array)
    print(f'Sorted array: {array}')

    # This code is contributed by Adnan Aliakbar