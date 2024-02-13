def build_next(c1):
    """计算字符串的next数组"""
    (prefix_len, i) = (0, 1)  #prefix_len是前缀的比较指针，也表示当前的共同前后缀长度
    next = [0]
    while i < len(c1):
        if c1[i] == c1[prefix_len]:
            prefix_len += 1
            next.append(prefix_len)
            i += 1
        else:  #匹配失败时
            if prefix_len == 0:
                next.append(0)
                i += 1
            else:
                prefix_len = next[prefix_len - 1]
    return next

def KMP_match(text,match):
    next = build_next(match)
    (i, j) = (0, 0)
    while i < len(text):
        if text[i] == match[j]: #字符匹配，比较下一个字符
            (i, j) = (i + 1,j + 1)
        elif j == 0: #match首字符失配
            i += 1
        else:
            j = next[j - 1]

        if j >= len(match): #match字符匹配完
            return i - j
    return -1

if __name__ == "__main__":
    text = "addadabaabacabababa"
    matchstring = "abacabab"
    print(KMP_match(text,matchstring))
