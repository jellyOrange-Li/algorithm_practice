def Chinaleave(mod_num, rem_num):
    """分别传入mod和余数列表"""
    M = 1  # M为所有mod之积
    result = 0
    for i in range(n):
        M *= mod_num[i]
    Mi = [0] * n
    Mi_ = [0] * n
    for i in range(n):
        Mi[i] = M // mod_num[i]
        Mi_[i] = pow(Mi[i], -1, mod_num[i])
    for i in range(n):
        result += Mi[i] * Mi_[i] * rem_num[i]
    return result % M

if __name__ == "__main__":
    mod_num = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    rem_num = [1, 2, 4, 4, 0, 10, 0, 18, 15, 16, 27, 22, 1, 11, 5]

    n = len(mod_num)
    print(Chinaleave(mod_num, rem_num))



