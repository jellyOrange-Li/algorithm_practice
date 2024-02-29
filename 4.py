# 递归回溯思想解决n皇后问题，cur代表当前行，从0开始一行行遍历
def queen(A, cur=0):
    # 判断上行放置的棋子是否有问题，如果有则回退
    for row in range(cur-1):
        # 由于是一行行遍历肯定不存在同行，只需检测是否同列和同对角线
        # 若在该列或对角线上存在其他皇后
        if A[row] == A[cur-1] or abs(A[row] - A[cur-1]) == abs(cur - 1 - row):
            # 该位置不能放
            return
    # 所有的皇后都正确放置完毕，输出每个皇后所在的位置
    if cur == len(A):
        print(A)
        return
    # 行数=列数，遍历每列
    for col in range(len(A)):
        # 当前行存储皇后所在的列数
        A[cur] = col
        # 继续放下一个皇后
        queen(A, cur+1)

# n为8，就是著名的八皇后问题啦
n = int(input())
# 初始传入8行的数组
queen([None] * n)