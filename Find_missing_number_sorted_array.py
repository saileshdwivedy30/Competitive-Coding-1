# Missing_number_sorted_array

# TC - O(log n)
# SC - O(1)

def missingNumber(arr):
    # code here

    low = 0
    high = len(arr) - 1

    while low <= high:

        mid = (low + high) // 2

        if arr[mid] == mid + 1:
            low = mid + 1
        else:
            high = mid - 1
    return low + 1
