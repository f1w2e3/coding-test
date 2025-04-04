#문제 1     N원을 거슬러 줘야 할 떄, 필요한 동전 최소 수를 구하세요 
# N = 1200 , 동전은 500원 100원이 있습니다.

N = 1200
coins = [500, 100]
count = 0

for coin in coins:
    while N >= coin:
        N -= coin
        count += 1

print(count)

#문제 2     N = 25    K = 3 일때  N이 1이 될때까지 나누기와 뺏셈을 사용하는는 프로그램을 짜세요.

N = 25
K = 3

count = 0

while N > 1:
    if N % K == 0:
        N = N // K
    else:
        N -= 1
        count += 1

print(count)
