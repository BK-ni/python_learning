nums = [1,3,4,5,6,7,2,9]
numMap = {}
n = len(nums)

# Build the hash table
for i in range(n):
    numMap[nums[i]] = i
    print(numMap)