
#문제1. 그리디 알고리즘과 최적해의 조건
#다음 프로그램은 사용자로부터 금액과 동전 단위들을 입력받습니다. 
#(입력 조건: 동전 단위는 1원을 포함하여 2개 이상의 단위들을 오름차순으로 입력받음)
#이때 그리디 알고리즘을 이용해 최소 동전 개수들로 n원을 만드는 방법은 다음과 같습니다.
'''
total=int(input("금액을 입력하세요"))
unit=input("동전 단위들을 작은 금액부터 입력하세요. 예: (1,100,200,400)")

unitarray=list(map(int,unit.strip("()").split(",")))

def greedy(x,num,total):
    num=num+total//unitarray[x-1]
    total=total%unitarray[x-1]
    return greedy(x-1,num,total) if x>=2 else num

num=greedy(len(unitarray),0,total)
print(f"{total}원을 만들기 위한 최소 동전 개수는 {num}개 입니다")
'''
#사용자의 금액 입력값은 5원 이상, 동전 단위 입력값은 <보기>와 같을 때 그리디 알고리즘이 최적해를 보장하지 않는 경우를 모두 고르시오.
# <보기>:
# (1). (1,100,200,400)
# (2). (1,100,200,500)
# (3). (1,20,50,70,100)
# (4). (1,5,25,75,150)
# (5). (1,17,170,340)

정답: 2,3,4

#문제2. 재귀함수
#사용자로부터 입력받은 n개의 정수를 원소로 갖는 집합의 모든 부분집합들을 출력하는 프로그램을 작성하세요.
#조건: 재귀함수를 사용하여 구현하기

def generate_subsets(arr, index, current):
    if index == len(arr):
        print(current)
        return
    generate_subsets(arr, index + 1, current)
    generate_subsets(arr, index + 1, current + [arr[index]])

n = int(input("원소 개수 입력: "))
elements = list(map(int, input(f"{n}개의 정수를 공백으로 입력: ").split()))

print("모든 부분집합:")
generate_subsets(elements, 0, [])