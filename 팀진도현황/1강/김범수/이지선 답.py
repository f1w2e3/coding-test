#문제 1:
#1부터 5까지 합을 계산하는 프로그램을 짜세요
#배열 변수는 array로 하고 합을 저장하는 변수를 summary로 설정을 하세요.

array = [1,2,3,4,5]
summary = 0

for i in range(5):
    summary = summary + array[i]

    print(summary)