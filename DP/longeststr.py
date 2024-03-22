def L(nums, i):
    """从序列的第i个元素起，返回最长的子序列长度"""
    if i == len(nums) - 1:
        return 1

    if i in memo:  #查字典
        return memo[i]

    max_len = 1
    for j in range(i + 1,len(nums)): #检查i后面所有数字
        if nums[j] > nums[i]:
            max_len = max(max_len, L(nums, j) + 1)
    memo[i] = max_len
    return max_len

def length_of_LIS(nums):
    return max(L(nums,i) for i in range(len(nums)))

if __name__ == "__main__":
    nums = [2, 1, 5, 2, 4, 3, 6]
    memo = {}     #DP字典
    print(length_of_LIS(nums))

# def length_of_nums(nums):
#     n = len(nums)
#     L = [1] * n
#     for i in reversed(range(n)):
#         for j in range(i + 1, n):
#             if nums[i] < nums[j]:
#                 L[i] = max(L[i], L[j] + 1)
#     return max(L)
#
#
# if __name__ == "__main__":
#     nums = [0, 2, 1, 5, 2, 4, 3, 6, 7]
#     print(length_of_nums(nums))














