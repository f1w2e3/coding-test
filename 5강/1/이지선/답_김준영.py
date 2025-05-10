# 이진 탐색 문제
# numbers 숫자 리스트를 만들고, 찾고 싶은 숫자 target을 지정하세요.
# 이진 탐색 방법을 이용하여 target이 리스트 안에 있으면 "찾음", 없으면 "없음"을 출력하세요.

# 조건
# numbers는 오름차순 정렬된 정수 리스트다.
# 1 ≤ len(numbers) ≤ 100
# target은 정수다.

numbers=[1,2,3,4,5]

target=2

def binary_search(start,end):
    point=numbers[end//2]
    if target==point:
        print(target)
        return
    
    if point>target:
        binary_search(start,point)
    elif point<target:
        binary_search(point,end)

binary_search(0,len(numbers)-1)

