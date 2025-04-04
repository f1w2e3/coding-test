
#문제 1     N원을 거슬러 줘야 할 떄, 필요한 동전 최소 수를 구하세요 
# N = 1200 , 동전은 500원 100원이 있습니다.

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




#문제 2     N = 25    K = 3 일때  N이 1이 될때까지 나누기와 뺏셈을 사용하는는 프로그램을 짜세요.
'''
def f(x,count):
    count=count+x%3
    return f(x//3,count) if x>=3 else count
print(f"최소 연산 횟수는 {f(25,0)}")
'''