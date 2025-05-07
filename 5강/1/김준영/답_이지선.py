# 문제1: 이진 탐색을 재귀적으로 구현하세요

def binary_search_recursive(numbers, target, left, right):
    if left > right:
        return -1
    mid = (left + right) // 2
    if numbers[mid] == target:
        return mid
    elif numbers[mid] < target:
        return binary_search_recursive(numbers, target, mid + 1, right)
    else:
        return binary_search_recursive(numbers, target, left, mid - 1)

numbers = [1, 3, 5, 7, 9, 11]
target = 7
result = binary_search_recursive(numbers, target, 0, len(numbers) - 1)
print(result)

# 문제2: 주어진 정렬된 배열에서 특정 값이 첫 번째로 등장하는 위치를 찾는 문제를 해결하세요.
# 입력:
# 정렬된 배열 arr (오름차순)
# 정수 target (찾을 값)
# 출력:
# target이 배열에 등장하는 첫 번째 인덱스를 반환하세요. 만약 target이 존재하지 않으면 -1을 반환하세요.

# 예시:
# arr = [1, 2, 2, 2, 3, 4]
# target = 2
# 출력: 1 (첫 번째 2가 1번 인덱스에 존재)

def find_first_index(arr, target):
    left = 0
    right = len(arr) - 1
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            result = mid
            break 
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return result

arr = [1, 2, 2, 2, 3, 4]
target = 2
print(find_first_index(arr, target)) 