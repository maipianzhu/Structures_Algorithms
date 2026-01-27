"""
LCP算法
"""


def lcp(s: str):
    n = len(s)
    lcp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n - 1, -1, -1):
        for j in range(n - 1, i, -1):
            if s[i] == s[j]:
                lcp[i][j] = lcp[i + 1][j + 1] + 1
            else:
                lcp[i][j] = 0
    return lcp


print(lcp("ababababcscbabscsbababs"))
