"""
管道问题
典型的二分法和线段覆盖问题
"""


def check(x):
    result = []
    for i in range(n):
        if x >= Si[i]:
            result.append((Li[i] - (x - Si[i]), Li[i] + (x - Si[i])))
    result.sort()
    if len(result) == 0 or result[0][0] > 1:
        return 0
    cc = result[0][1]
    for j in range(1,len(result)):
        if cc + 1 >= result[j][0]:
            cc = max(cc, result[j][1])
        else:
            return 0
    return cc >= m

n, m = 3, 10
Li = [1, 6, 10] # 段数
Si = [1, 5, 2] # 开启时间
l = 1
r = 2_000_000_000
while l < r:
    mid = (l + r) // 2
    if check(mid): #如果mid可以
        r = mid
    else:
        l = mid + 1
print(r)







