# #문제1.
# 문자열 s가 주어졌을 때, 괄호가 올바르게 열리고 닫혔는지 판별하는 함수 만들기.
# 예를 들어 "()", "(())()"는 올바르지만, ")(", "(()"는 올바르지 않음.



# 예시
# is_valid_parentheses("()()") ➞ True  
# is_valid_parentheses("(())()") ➞ True  
# is_valid_parentheses("(()") ➞ False  
# is_valid_parentheses(")(") ➞ False

def is_valid_parentheses(s):
    count = 0  
    for char in s:
        if char == '(':
            count += 1
        elif char == ')':
            count -= 1
        if count < 0:
            return False
    return count == 0


# #문제2.
# 주어진 숫자 리스트가 있을 때 숫자들 앞에 + 또는 -를 붙여서 타겟 숫자를 만들 수 있는 경우의 수를 구하라.

# 예시
# numbers = [1, 1, 1, 1, 1]
# target = 3

# 출력
# 5
# 설명: 다음과 같은 5가지 방법이 있음
# +1 +1 +1 -1 +1 = 3
# +1 +1 -1 +1 +1 = 3
# +1 -1 +1 +1 +1 = 3
# -1 +1 +1 +1 +1 = 3
# +1 +1 +1 +1 -1 = 3

def count_ways(numbers, target):
    def dfs(i, total):
        if i == len(numbers):
            return 1 if total == target else 0
        return dfs(i + 1, total + numbers[i]) + dfs(i + 1, total - numbers[i])
    return dfs(0, 0)