# 퀵 정렬을 이용하여 숫자 리스트를 오름차순으로 정렬하세요.
# 입력: 5 3 8 4 2 
# 출력: [2, 3, 4, 5, 8]


# 삽입 정렬을 이용하여 숫자 리스트를 오름차순으로 정렬하세요.
# 입력: 4 1 3 9 2
# 출력: {1, 2, 3, 4, 9}



#선택 정렬:
#테스트용: array=[7,5,9,0,3,1,6,2,4,8]

array=list(map(int,input().split(" ")))

def find_small_index(x):
    #x부터 len(array) 까지 중 가장 작은 값의 인덱스 찾기
    front=array[x]
    index=x
    for _ in range(x+1,len(array)):
        if array[_]<front:
              front=array[_]
              index=_
    return index

for x in range(len(array)):
    temp=array[x]
    small_index=find_small_index(x)
    array[x]=array[small_index] #x+1부터 len(array)까지 중 가장 작은 애 
    array[small_index]=temp

print(array)



문제1:
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]  
    left = [x for x in arr[1:] if x <= pivot]  
    right = [x for x in arr[1:] if x > pivot]  
    return quick_sort(left) + [pivot] + quick_sort(right)

array = list(map(int, input().split()))
print(quick_sort(array)) 


문제2:
def insertion_sort(arr):
    for i in range(1, len(arr)):
        for j in range(i, 0, -1): 
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
            else:
                break
    return arr

array = list(map(int, input().split()))  
print(insertion_sort(array)) 