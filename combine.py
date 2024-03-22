class Solution:
    def __init__(self):
        self.result = []

    def combine(self, n: int, k: int):
        self.trackbacking(n, k, 1, [])
        print(self.result)

    def trackbacking(self, n: int, k: int, now, cur):
        if len(cur) == k:
            self.result.append(cur[:])
            return
        for i in range(now, n - k + len(cur) + 2):    # i + (k - len(cur)) <= n + 1
            cur.append(i)
            self.trackbacking(n, k, i + 1, cur)
            cur.pop()

solution = Solution()
solution.combine(5, 2)

