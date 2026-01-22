"""
KMP 算法（Knuth-Morris-Pratt 算法）是计算机科学中非常经典、也非常巧妙的字符串匹配算法。
它的主要用途是：在一个长字符串（主串）中，找到一个短字符串（模式串）出现的位置。
"""

"""
    AI全文背诵版本,构造记录数组
"""


def get_next(pattern):
    n = len(pattern)
    next_arr = [0] * n

    # j 代表前缀的末尾位置（也等于当前匹配的长度）
    # i 代表后缀的末尾位置
    j = 0

    # i 从 1 开始遍历
    for i in range(1, n):
        # 1. 如果不匹配，就一直回退 j，直到 j 回到 0 或字符匹配为止
        while j > 0 and pattern[i] != pattern[j]:
            j = next_arr[j - 1]

        # 2. 如果匹配成功，前缀长度 j 加 1
        if pattern[i] == pattern[j]:
            j += 1

        # 3. 记录结果
        next_arr[i] = j

    return next_arr


# --------------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    # 主串
    text = "abababaababcabb"
    # 模式串
    pattern = "ababc"

    recod = [0] * len(pattern)

    j = 0

    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = recod[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
        recod[i] = j

    j = 0
    for i in range(len(text)):
        while j > 0 and text[i] != pattern[j]:
            j = recod[j - 1]
        if text[i] == pattern[j]:
            j += 1
        if j == len(pattern):
            print(i - j + 1)
            break
