#문제1. 주어진 배열에서 가장 작은 수의 합을 구하세요
#A = [1, 2, 3] , B = [3, 2 1]

A = [1, 2, 3]
B = [3, 2, 1]

min_A = min(A)
min_B = min(B)

result = min_A + min_B

print("가장 작은 수의 합: ", result)

#문제2. 500원, 50원, 10원 동전이 있을 때, 주어진 금액을 거슬러 주기 위해 필요한 최소 동전 개수를 구하시오.
#금액:1580

money = 1500
coins = [500, 50, 10]
count = 0

for coin in coins:
    count += money // coin 
    money %= coin 

print("필요한 최소 동전 개수: ", count)