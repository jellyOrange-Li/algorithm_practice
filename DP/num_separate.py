"""
数字划分
使用一维数组，求将数字拆成任意个数字并相乘所得的积的最大值
对于数字i，遍历将其拆为j和i-j的最大值，并与dp[i-j]的对比
相当于看是否拆成两个以上的数字可能为结果，dp[i-j]就已经包括了拆成多个的最大
"""
if __name__ == "__main__":
    dp = [0] * 20
    dp[2] = 1
    for i in range(3,20):
        for j in range(1, i):
            dp[i] = max(dp[i],max((i - j) * j, dp[i - j] * j))
    print(dp)

