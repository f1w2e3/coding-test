# 문제1. 0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.

# 답:def factorial(n):
#     result = 1
#     for i in range(2, n + 1):
#         result *= i
#     return result

# N = int(input("정수 N을 입력하세요: "))
# print(factorial(N))

# 문제2. 문자 A,B,C,D,E를 스택에 넣었다가 다시 꺼내 출력하면 어떻게 되는가?
# 답: E,D,C,B,A