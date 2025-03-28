#time 알고리즘을 사용해서 수행시간을 출력해보세요.
# 준영님 1번 문제 수행시간을 출력해 보았습니다!

import time

n = input("입력: ")
start = time.time()

sum_digits = 0
for digit in n:
    sum_digits += int(digit)
end = time.time()

print("출력: ", sum_digits)
print("수행시간:", round(end - start, 5), "초")