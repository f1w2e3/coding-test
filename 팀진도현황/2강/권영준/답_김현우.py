
#첫째 줄에 모험가의 수 N이 주어집니다 (1<= N <= 100000)
#둘째 줄에 각 모험가의 공포도의 값을 N 이하의 자연수로 주어지며, 각 자연수는 공백으로 구분합니다.
#여행을 떠날 수 있는 그룹 수의 최댓값을 출력합니다

n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0
cnt = 0

for i in data:
    cnt += 1
    if(cnt >= i):
        result += 1
        cnt = 0
print(result)

#첫째 줄에 공간의 크기를 나타내는 N이 주어집니다. (1 <= N <= 100)
#둘째 줄에 여행가 A가 이동할 계획서 내용이 주어집니다(1 <= 이동 횟수 <= 100)
#첫째 줄에 여행가 A가 최종적으로 도착할 지점의 좌표(X, Y)를 공백을 기준으로 구분하여 출력합니다.
#입력예시
# 5
# R R R U D D

n = int(input())

x, y = 1, 1
plans = input().split()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

move_type = ['L', 'R', 'U', 'D']

for plan in plans:
  for i in range(len(move_type)):
    if plan == move_type[i]:
      nx = x + dx[i]
      ny = y + dy[i]

  if nx < 1 or ny < 1 or nx > n or ny > n:
    continue

  x, y = nx, ny

print(x, y)