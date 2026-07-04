##Thực chiến LeetCode
##Bài tập về duyệt mảng: 
# 1295. Find Numbers with Even Number of Digits



# def array_A(ListA):
#     count = 0
#     for i in range(len(ListA)):
#         if len(str(ListA[i])) % 2 == 0:
#             count += 1
#     return count
# listA = [12, 345, 2, 6, 7896]
# result = array_A(listA)
# print(result)  # Output: 2



from unittest import result


class Solution(object):
    def findNumbers(self, nums):
        count = 0
        for i in range(len(nums)):
            if len(str(nums[i])) % 2 == 0:
                count += 1
        return count
        
nums = [12, 345, 2, 6, 7896]
result = Solution().findNumbers(nums)
print(result)  # Output: 2