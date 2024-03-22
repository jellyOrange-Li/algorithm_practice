"""
三国游戏
看数据范围想方法，一般数据越大方法越简单，越小也简单
利用计算机解决问题的特性，可以分魏蜀吴赢三种情况讨论，然后比较出最大值
列表排序、倒序很有用
"""
def sanguo(a, b, c)->int:
    ans = []
    for i in range(n):
        ans.append(a[i] - b[i] - c[i])
    ans.sort(reverse = True)
    sum, res = 0, -1
    for i in range(n):
        sum += ans[i]
        if sum > 0:
            res = i + 1  #妙蛙
    return res

if __name__ == "__main__":
    n = int(input("n:"))
    A = list(map(int, input("A:").split(" ")))
    B = list(map(int, input("B:").split(" ")))
    C = list(map(int, input("C:").split(" ")))
    print(max(sanguo(A,B,C), sanguo(B,A,C), sanguo(C,A,B)))


