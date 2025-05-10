#첫째 줄에 모험가의 수 N이 주어집니다 (1<= N <= 100000)
#둘째 줄에 각 모험가의 공포도의 값을 N 이하의 자연수로 주어지며, 각 자연수는 공백으로 구분합니다.
#여행을 떠날 수 있는 그룹 수의 최댓값을 출력합니다

#입력 예시
# 5
# 2 3 1 2 2

'''
from collections import Counter

n = input()
n = list(map(int, n.split()))

counts = Counter(n)

key = list(counts.keys())
value = list(counts.values())

def f(x, result, people):
    if x == len(key):   # 종료 조건 먼저!
        return result
    result += (value[x] + people) // key[x]
    people = (value[x] + people) % key[x]
    return f(x + 1, result, people)

result = f(0, 0, 0)
print(result)
'''


#첫째 줄에 공간의 크기를 나타내는 N이 주어집니다. (1 <= N <= 100)
#둘째 줄에 여행가 A가 이동할 계획서 내용이 주어집니다(1 <= 이동 횟수 <= 100)
#첫째 줄에 여행가 A가 최종적으로 도착할 지점의 좌표(X, Y)를 공백을 기준으로 구분하여 출력합니다.
#입력예시
# 5
# R R R U D D


'''
n = int(input("숫자 입력: "))
space = [[0 for _ in range(n)] for _ in range(n)]

control = input("이동 입력 (예: R R U D): ").split()

x, y = 0, 0

for direction in control:
    # 이동 전 임시 좌표 계산
    nx, ny = x, y
    if direction == 'R':
        nx += 1
    elif direction == 'L':
        nx -= 1
    elif direction == 'U':
        ny -= 1  
    elif direction == 'D':
        ny += 1  

    if 0 <= nx < n and 0 <= ny < n:
        x, y = nx, ny


space[y][x] = 1


for row in space:
    print(row)

print(f"최종 위치: ({x}, {y})")
'''