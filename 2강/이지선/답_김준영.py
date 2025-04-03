# 그리디 알고리즘 문제 
# 다음 리스트가 주어졌을때, 가장 큰 수 하나를 제외하고 나머지 수들을 모두 더한 값을 구하는 코드를 입력하세요.
# 입력 : nums = [5, 1, 9, 3, 7]
# 출력 : 16 
'''
big_num=0
sum=0
nums = [5, 1, 9, 3, 7]
for _ in range(len(nums)):
        if big_num<nums[_]:
              big_num=nums[_]

for _ in range(len(nums)):
       sum=sum+nums[_]
print(sum-big_num)
'''


# 구현 문제
# 사용자가 입력한 숫자를 리스트에 추가한 후, 그 리스트를 출력하는 프로그램을 작성하세요.
# 1. 리스트는 비어있다.
# 2. 사용자가 입력한 숫자는 1개만 추가된다.
# 3. 숫자는 0 이상 100 이하로 입력된다.
# 입력예시: numbers = [] 
# 출력예시: [20]  (사용자가 입력한 수가 20일 경우우)
'''
numbers=[]
n=int(input())
if 0<n<100:
    numbers.append(n)
print(numbers)
'''