from collections import deque


def bfs_matrix(grid, start_r, start_c):
    rows, cols = len(grid), len(grid[0])
    queue = deque([(start_r, start_c)])

    # 标记已访问（或者直接修改 grid[start_r][start_c] = '0'）
    grid[start_r][start_c] = "0"

    # 方向向量：上下左右
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    area = 1  # 如果是算面积

    while queue:
        r, c = queue.popleft()

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            # 边界检查 + 业务条件判断
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1":
                # 【核心避坑】入队即标记！
                grid[nr][nc] = "0"
                queue.append((nr, nc))
                area += 1

    return area
