from itertools import product

def count_ways():
    total_ways = 0
    for candies in product(range(2, 6), repeat=7):  # 生成所有可能的糖果分配方式
        if sum(candies) == 25:  # 确保总糖果数为25（9+16）
            total_ways += 1
    return total_ways

