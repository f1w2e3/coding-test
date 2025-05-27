#피보나치 구현방법

#재귀:
def fib(now, ahead_2, ahead_1,end):
    result=ahead_2+ahead_1
    ahead_2=ahead_1
    ahead_1=result
    if now==end:
        return result
    now+=1
    return fib(now, ahead_2, ahead_1,end) 

end=8
fib(3,1,1,end)


#dp 탑다운
d=[0]*100
d[0]=1
d[1]=1
n=99
def fib(n):
    if d[n]!=0:
        return d[n]
    d[n]=fib(n-1)+fib(n-2)
    return d[n]

print(fib(99))


#dp 바텀업
d=[0]*100
d[0]=1
d[1]=1
n=99
for i in range(2,n+1):
    d[i]=d[i-1]+d[i-2]
print(d[n])


