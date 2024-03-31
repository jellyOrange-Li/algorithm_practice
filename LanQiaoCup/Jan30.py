def BubbleSort(lst):
    n = len(lst)
    if n <= 1:
        return lst
    for i in range(0,n-1):
        for j in range(0,n-i-1):
            if lst[j] > lst[j+1]:
                (lst[j],lst[j+1])=(lst[j+1],lst[j])
    return lst

def FastSort(arr): #头尾指针分别指向序号为m，n
    def participate(m,n):
        while m < n:
            while m < n and arr[m] <= arr[n]:
                n = n - 1
            while m < n and arr[m] <= arr[n]:
                m = m + 1
            (arr[m], arr[n]) = (arr[n], arr[m])
        return m

    def fastsort(m,n):
        if m >= n:
            return
        a = participate(m,n)
        fastsort(m,a-1)
        fastsort(a+1,n)

    n = len(arr)
    if n <= 1:
        return arr
    fastsort(0,n-1)
    return arr

if __name__ == '__main__':
    x = input("请输入待排序的数字，用空格分隔")
    x = x.split()
    w = []
    for i in x:
        w.append(int(i))
    # w = BubbleSort(w)
    w = FastSort(w)
    print(w)

