

"""
round函数取整
input返回结果要int()
"""



if __name__ == "__main__":
    n = int(input())
    #及格人数
    passNum = 0
    #优秀人数
    goodNum = 0
    for _ in range(n):
        score = int(input())
        if score >= 60 :
            passNum += 1
        if score >= 85 :
            goodNum += 1
    print(passNum * 100 // n,'%')
    print(str(round(passNum / n * 100))+'%')








