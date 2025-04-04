#첫째 줄에 모험가의 수 N이 주어집니다 (1<= N <= 100000)
#둘째 줄에 각 모험가의 공포도의 값을 N 이하의 자연수로 주어지며, 각 자연수는 공백으로 구분합니다.
#여행을 떠날 수 있는 그룹 수의 최댓값을 출력합니다

#입력 예시
# 5
# 2 3 1 2 2

N = int(input())
fears = sorted(map(int, input().split))

group, count = 0, 0
for f in fears:
    count += 1
    if count >= f:
        group += 1
        count = 0

print (group)

#첫째 줄에 공간의 크기를 나타내는 N이 주어집니다. (1 <= N <= 100)
#둘째 줄에 여행가 A가 이동할 계획서 내용이 주어집니다(1 <= 이동 횟수 <= 100)
#첫째 줄에 여행가 A가 최종적으로 도착할 지점의 좌표(X, Y)를 공백을 기준으로 구분하여 출력합니다.
#입력예시
# 5
# R R R U D D

N = int(input())
moves = input().split()

x, y = 1, 1

for move in moves:
    if move == 'L' and y > 1:
        y -= 1
    elif move == 'R' and y < N:
        y += 1
    elif move == 'U' and x > 1:
        x -= 1
    elif move == 'D' and x < N:
        x += 1

print(x, y)