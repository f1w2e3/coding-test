#문제 3
#재귀함수를 호출합니다.라는 문자열을 무한히 출력하세요

def print2(x):
    print("재귀함수를 호출합니다.")
    print2(x+1) if x<=10 else ""
print2(1)


#문제4
#첫번째 줄에 얼음 틀의 세로 길이 N과 가로 길이 M이 주어집니다(1<=N, M<= 1000)
#두번째 줄부터 N+1번쨰 줄까지 얼음 틀의 형태가 주어집니다
#이때 구멍이 뚫려있는 부분은 0, 그렇지 않는 부분은 1입니다.
#한 번에 만들 수 있는 아이스크림의 개수를 출력하세요

#입력 에시
#4 , 5
#00110
#00011
#11111
#00000

n, m = map(int, input().split())
graph = [list(map(int, list(input()))) for _ in range(n)]


def dfs(x, y):

    if x < 0 or x >= n or y < 0 or y >= m:
        return False

    if graph[x][y] == 0:
        graph[x][y] = 1 
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
    return False


count = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j): 
            count += 1

print(count)
