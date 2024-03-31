"""
和的树状数组：
1.创建的tree列表大小为N+1 用update初始化;nums记录当前真实数组中存储的值(起始为0是为了初始化)，也是为了后续再对tree修改时计算delta用
2.update初始化时i=index+1,是为了让tree从tree[1]开始更改
3.因为tree整体向后移了一位，将第一位空位置零;所以sumer求和也需要将x加1;或者在sumRange直接对传入sumer的参数加1也可以

"""

class NumArray:
    def __init__(self, nums):
        self.N = len(nums)
        self.nums = [0] * self.N
        self.tree = [0] * (self.N + 1)
        for i,r in enumerate(nums):
            self.update(i, r)

    def update(self, index: int, val: int) -> None:
        delta = val - self.nums[index]
        self.nums[index] = val
        i = index + 1
        while i <= self.N:
            self.tree[i] += delta
            i += i & -i

    def sumRange(self, left: int, right: int) -> int:
        return self.sumer(right) - self.sumer(left - 1)

    def sumer(self, x):
        x += 1
        ans = 0
        while x:
            ans += self.tree[x]
            x -= x & -x
        return ans


obj = NumArray([1,3,5])
print(obj.tree)
print(obj.sumRange(0,2))
obj.update(1,2)
print(obj.sumRange(0,2))







