
"""
不必保存之前的结果
直接对result操作就可以
创建result为空字符串类型
"""


if __name__ == "__main__":
    n = int(input())
    result = ''
    for i in range(n):
        result = result + chr(ord('A') + i) + result
        print('"' + result + '"')



