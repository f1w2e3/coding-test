#N = 25    K = 3 일때  N이 1이 될때까지 나누기와 뺏셈을 사용하는는 프로그램을 짜세요.

N = 25
K = 3
count = 0

while N > 1:
    if N % K != 0:
        N -= 1
    else:
        N //= K
    count += 1
print(count)

 N원을 거슬러 줘야 할 떄, 필요한 동전 최소 수를 구하세요 
# N = 1200 , 동전은 500원 100원이 있습니다.

n=1200
count = 0
array = [500, 100]
for coin in array:
    count += n // coin
    n %= coin
print(count)
