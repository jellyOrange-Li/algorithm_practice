def insertSort(arr): #每次从后面拿一个按大小顺序插入
    n = len(arr)
    if n <= 1:
        return arr
    for t in range(1,n):
        i = t
        while i > 0 and arr[i-1] > arr[i]:
            (arr[i-1],arr[i]) = (arr[i],arr[i-1])
            i = i - 1
    return arr

def SelectSort(arr): #每次选择最小的放在前面
    n = len(arr)
    if n <= 1:
        return arr
    for i in range(0,n):
        choice = i
        for j in range(i+1,n):
            if arr[choice] > arr[j]:
                choice = j
        if i != choice:
            (arr[i],arr[choice]) = (arr[choice],arr[i])
    return arr

def shellSort(arr):  #希尔排序
    def shellinsert(lst,dd):
        for i in range(0,n):
            choice = i
            for j in range(i+dd,n,dd):
                if lst[choice] > lst[j]:
                    choice = j
            if i != choice:
                (lst[i],lst[choice]) = (lst[choice],lst[i])
        return lst

    n = len(arr)
    if n <= 1:
        return arr
    d = (n + 1) // 2
    while d >= 1:
        arr = shellinsert(arr,d)
        d = d // 2
    return arr

if __name__ == "__main__":
    w = input("按序输入待排序的数字，空格分隔")
    w = w.split()
    x = []
    for i in w:
        x.append(int(i))
    x = shellSort(x)
    print(x)


