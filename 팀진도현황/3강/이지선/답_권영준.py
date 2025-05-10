# 재귀함수 문제
# 양의 정수 n이 주어졌을 때, n!(팩토리얼)을 재귀함수를 이용해서 구해보세요.
# 입력 예시: 3
# 출력 예시: 6

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
n = 3
print(f"{n}! = {factorial(n)}")

# BFS 문제
# 1에서 시작해서 5까지 가는 최소 이동 횟수의 경로를 BFS 알고리즘을 이용해 구해보세요.
# 조건 - 현재 숫자에서 +1 또는 +2만 가능
#      - 숫자는 중복 방문하지 않아야 함
#      - 도착 숫자인 5에 도달하면 탐색 종료
# 출력 예시: 1 → 2 → 3 → 4 → 5

from collections import deque

def bfs(start, target):
    queue = deque([(start, [start])])
    visited = set()
    
    visited.add(start)

    while queue:
        current, path = queue.popleft()

        if current == target:
            return path
        
        for next_num in (current + 1, current + 2):
            if next_num <= target and next_num not in visited:
                visited.add(next_num)
                queue.append((next_num, path + [next_num]))
    return [] 

start = 1
target = 5
result = bfs(start, target)

print(" → ".join(map(str, result)))