def two_sum(numbers, target):
    result = []
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                result.append(i)
                result.append(j)
                return result


            
numbers = [2, 7, 11, 15]
target = 9
result = two_sum(numbers, target)
print(result)  # Output: [0, 1]

for i in result:
    print(f"Index: {i}, Value: {numbers[i]}")