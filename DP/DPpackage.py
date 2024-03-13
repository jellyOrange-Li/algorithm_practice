#
# if __name__ == "__main__":
#     # 各物品重量及价值
#     weight = [1, 3, 4]
#     value = [15, 20, 30]
#     # 背包最大容量
#     bagweight = 4
#
#     # dp[i][j] 表示从下标为[0~i]的物品里任意取，放进容量为j的背包，价值总和最大是多少
#     # 是由正上方和左上方某个值确定的 -> 行列先后不影响
#     dp = [[0 for col in range(bagweight+1)] for row in range(len(weight))]
#     for i in range(weight[0], bagweight + 1):
#         dp[0][i] = value[0]
#
#     # 遍历物品
#     for j in range(1, bagweight + 1):  # 先遍历行再遍历列
#         for i in range(1, len(weight)):
#             if j < weight[i]:
#                 dp[i][j] = dp[i - 1][j]  # 如果上一个物品比这个大，那么正上方的数也没计入上一个物品的重量
#             else:
#                 dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight[i]] + value[i])
#
#     print(dp[len(weight)-1][bagweight])
#     print(dp)


if __name__ == "__main__":
    weight = [1, 3, 4]
    value = [15, 20, 30]
    bagweight = 4

    dp = [0 for _ in range(bagweight + 1)]

    for i in range(len(weight)): #先列后行;先容量后物品
        for j in range(weight[i], bagweight + 1): # 从前到后是完全背包解法，从后道前是01背包
            dp[j] = max(dp[j], dp[j-weight[i]] + value[i])
    print(dp)













