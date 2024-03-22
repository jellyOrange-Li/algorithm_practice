"""
递归的思想，用cur标记当前行，在函数末尾进行递归，并在函数首检查上一次是否出错
用于递归的函数放在逻辑末尾！！！而判断结束的语句放在前面
"""

def nqueen(A,cur = 0):
    # cur代表当前行，默认为0
    global num
    for row in range(cur-1): # 检测是否与之前的cur-1行矛盾
        if A[row] == A[cur-1] or abs(A[row] - A[cur-1]) == cur - 1 - row:
            return  # 不能放
    if cur == len(A):
        num += 1
        print(num,':',A)
        return
    for row in range(n):
        A[cur] = row
        nqueen(A,cur + 1)

if __name__ == "__main__":
    n = int(input("n:"))
    num = 0
    nqueen([None]*n)





