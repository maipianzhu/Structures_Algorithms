"""
Z算法
对于字符串 s，定义 z[i] 表示后缀 s[i:] 与 s 的 LCP（最长公共前缀）的长度，其中 s[i:] 表示从 s[i] 到 s[n−1] 的子串。
常用技巧是构造字符串 pattern+s，如果发现 z[m+i]≥m（m 是 pattern 的长度），则说明从 s[i] 开始的子串与 pattern 匹配。
"""


def z_algorithm(s: str) -> list[int]:
    z_next = [0] * len(s)
    left = 0
    right = 0
    for i in range(1, len(s)):
        if i <= right:
            z_next[i] = min(z_next[i - left], right - i + 1)

        while i + z_next[i] < len(s) and s[i + z_next[i]] == s[z_next[i]]:
            z_next[i] += 1

        if z_next[i] + i - 1 > right:
            right = z_next[i] + i - 1
            left = i
    return z_next


print(z_algorithm("ababababcscbabscsbababs"))
