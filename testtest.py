def permutaion(nums, cur, used):
    global result
    if len(cur) == len(nums):
        result.append(cur[:])
        return
    for i in range(0, len(nums)):
        if i > 0 and nums[i] == nums[i - 1] and used[i-1] == 0:
            continue
        if used[i] == 1:
            continue
        cur.append(nums[i])
        used[i] = 1
        permutaion(nums, cur, used)
        cur.pop()
        used[i] = 0

result = []
permutaion([1,1,1,2,2], [], [0] * len([1,1,1,2,2]))
print(result)










