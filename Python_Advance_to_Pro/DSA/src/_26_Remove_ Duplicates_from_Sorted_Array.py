def removeDuplicates(nums):
    # count = []
    # i = 0
    # for i in range(len(nums)):
    #     if nums[i] not in count:
    #         count.append(nums[i])
    #         i += 1
    # k = len(count)#list(set(count) ^ set(nums))
    # return count, k

    if len(nums) == 0:
        return 0
    k = 1
    for i in range(1, len(nums)):
        if nums[i]!= nums[i-1]:
            nums[k] = nums[i]
            k+=1       
    return k


nums = [1, 1, 2]
resuft = removeDuplicates(nums)
print(resuft)
print(nums[:resuft])
