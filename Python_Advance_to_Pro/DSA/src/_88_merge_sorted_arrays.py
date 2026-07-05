# Merge Sorted Arrays

def merge_sorted_arrays(nums1, nums2, m, n):
    # i, j = 0, 0
    # len(nums2) = n
    # k = m + n
    # len(nums1) = k



    i, j, k = m - 1, n - 1, m + n - 1
    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1
    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1



# Example usage:
nums1 = [1, 2, 5, 0, 0, 0]
nums2 = [2, 4, 6]
m = 3
n = 3
merged_array = merge_sorted_arrays(nums1, nums2, m, n)
print(nums1)  # Output: [1, 2, 2, 4, 5, 6]