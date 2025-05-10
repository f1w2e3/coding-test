
#참고: dfs로 상하좌우 검색하지 않고도 greedy 알고리즘으로 풀 수 있음


#문제 설명) 1은 땅, 0은 물로 이루어진 2차원 지도(grid)가 주어졌을 때, 섬의 개수를 구하는 함수를 작성하시오.
# 섬은 수직, 수평으로 연결된 땅들의 집합이며, 대각선은 연결로 간주하지 않습니다.

#제약 사항) 1 <= grid.length <= 100
# 1 <= grid[0].length <= 100
# 각 셀은 "0" 또는 "1" 의 문자열 형태임


def numIslands(grid):
    if not grid:
        return 0

    n, m = len(grid), len(grid[0])
    
    def dfs(i, j):
        if i < 0 or i >= n or j < 0 or j >= m or grid[i][j] != '1':
            return
        grid[i][j] = '0'
        dfs(i+1, j)
        dfs(i-1, j)
        dfs(i, j+1)
        dfs(i, j-1)

    count = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '1':
                dfs(i, j)
                count += 1

    return count