

def remove_element(nums, val):
    left = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[left] = nums[i]
            left += 1
    return left

nums = [1, 2, 2, 3, 1, 4, 5, 5, 6]
val = 1
k = remove_element(nums, val)
print(k)
print(nums[:k])