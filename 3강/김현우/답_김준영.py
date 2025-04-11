# 문제1. 0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.


def fac(x):
    if x > 1:
        return x * fac(x - 1)
    else:
        return 1

print(fac(10))



# 문제2. 문자 A,B,C,D,E를 스택에 넣었다가 다시 꺼내 출력하면 어떻게 되는가?

E D C B A
