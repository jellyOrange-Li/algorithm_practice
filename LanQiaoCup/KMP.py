def build_next(c1):
    """计算字符串的next数组"""
    """next数组代表在匹配失败时子串中可以跳过匹配的字符个数"""
    """next[i]数组的值就是字符[0]到[i]的最长相同前后缀的长度 -----> 为了在text的当前位置跳过match的前缀"""
    """如ABACABAB B与C失配->其他字符串在前面匹配时与C失配->看C前面的A的next值并继续匹配，主串指针不变"""
    (prefix_len, i) = (0, 1)  # prefix_len是前缀的比较指针，也表示当前的共同前后缀长度
    next = [0]
    while i < len(c1):
        if c1[i] == c1[prefix_len]:
            prefix_len += 1
            next.append(prefix_len)
            i += 1
        else:  #匹配失败时
            if prefix_len == 0: # 还未匹配成功
                next.append(0)
                i += 1
            else:
                prefix_len = next[prefix_len - 1]
    return next

def KMP_match(text,match):
    next = build_next(match)
    (i, j) = (0, 0) #i,j分别代表主串和字串指针 i永不递减
    while i < len(text):
        if text[i] == match[j]:
            i, j = i + 1, j + 1
        elif j == 0: # 首字符失配
            i += 1
        # 失配后直接将text[i]与next[next[j-1]]进行比较"""
        else:
            j = next[j - 1]

        if j >= len(match): # 匹配完成
            return i - j
    return -1

if __name__ == "__main__":
    text = "addadabaabacabababa"
    matchstring = "abacabab"
    print(KMP_match(text,matchstring))


# def pusu(string,match):
#     i, j = 0, 0            #i,j分别表示主串和子串中的指针
#     while i < len(string):
#         if string[i] == match[j]:
#             i = i + 1
#             j = j + 1
#         else:
#             i = i - j + 1
#             j = 0
#
#         if j == len(match):
#             return i - j
#     return -1
# if __name__ == "__main__":
#     stl = "aabbababb"
#     match = "babb"
#     print(pusu(stl, match))
