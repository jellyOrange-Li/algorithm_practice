def hanotower(n,a,b,c):
    """将n个圆环从a移到c"""
    global v
    if n <= 0:
        return
    elif n == 1:
        print(v,":",a,"--->",c)
    else:
        hanotower(n-1,a,c,b)    #将上面n-1个圆环移至中转柱
        hanotower(1,a,b,c)   #将最下面的移到目标位置
        hanotower(n-1,b,a,c)
    v = v + 1

if __name__ == "__main__":
    n = input("请输入圆环的数量:")
    v = 1
    hanotower(int(n),'a','b','c')