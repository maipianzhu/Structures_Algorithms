"""
Floyd-Warshall 算法（简称 Floyd 算法）是图论中用于解决多源最短路径（All-Pairs Shortest Path）问题的经典算法。
如果说 Dijkstra 是“以此处为起点，探索去往各地的最短路”，那么 Floyd 算法就是“上帝视角”，一次性计算出图中任意两个节点之间的最短距离。
1. 核心特点
功能：计算图中所有节点对
(i,j)
 之间的最短路径。
适用范围：
有向图或无向图。
正权边和负权边均可（Dijkstra 不能处理负权）。
注意：不能处理包含“负权环”（总和为负的回路）的图。
核心思想：动态规划（Dynamic Programming）。
2. 核心原理：中转点
Floyd 算法的本质非常直观，就一句话：
“两点之间，如果通过第三个点（中转点）走比直接走更近，那就走中转点。”
3. 算法步骤（三层循环）
"""

"""
给你两个下标从 0 开始的字符串 source 和 target ，它们的长度均为 n 并且由 小写 英文字母组成。

另给你两个下标从 0 开始的字符数组 original 和 changed ，以及一个整数数组 cost ，其中 cost[i] 代表将字符 original[i] 更改为字符 changed[i] 的成本。

你从字符串 source 开始。在一次操作中，如果 存在 任意 下标 j 满足 cost[j] == z  、original[j] == x 以及 changed[j] == y 。你就可以选择字符串中的一个字符 x 并以 z 的成本将其更改为字符 y 。

返回将字符串 source 转换为字符串 target 所需的 最小 成本。如果不可能完成转换，则返回 -1 。

注意，可能存在下标 i 、j 使得 original[j] == original[i] 且 changed[j] == changed[i]

"""


class Solution:
    def minimumCost(
        self,
        source: str,
        target: str,
        original: list[str],
        changed: list[str],
        cost: list[int],
    ) -> int:
        # 1. 初始化距离矩阵
        # 使用 float('inf') 代表无穷大
        inf = float("inf")
        dist = [[inf] * 26 for _ in range(26)]

        # 字母到自己的成本为 0
        for i in range(26):
            dist[i][i] = 0

        # 2. 填入初始给定的转换成本
        for o, c, w in zip(original, changed, cost):
            u = ord(o) - ord("a")
            v = ord(c) - ord("a")
            # 可能会有重复的转换规则，取最小的那个
            dist[u][v] = min(dist[u][v], w)

        # 3. Floyd-Warshall 算法：计算任意两点间的最短路径
        # k 是中间节点，i 是起点，j 是终点
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    # 如果经过 k 能使距离变得更短，则更新
                    # 只有当 dist[i][k] 和 dist[k][j] 都不是无穷大时才相加，防止 inf + inf
                    if dist[i][k] != inf and dist[k][j] != inf:
                        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

        # 4. 遍历字符串计算总成本
        total_cost = 0
        for s_char, t_char in zip(source, target):
            u = ord(s_char) - ord("a")
            v = ord(t_char) - ord("a")

            # 如果这两个字母之间不可达
            if dist[u][v] == inf:
                return -1

            total_cost += dist[u][v]

        return total_cost
