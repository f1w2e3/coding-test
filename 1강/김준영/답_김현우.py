#문제1: 그리디 알고리즘
#어떤 수 N이 주어졌을때 N의 모든 자릿수의 합을 구하는 프로그램을 작성하세요.

N = 12394
summary = sum(int(digit) for digit in str(N))
print(f"{N}의자릿수 합: {summary}")

#어떤 영어 단어를 입력했을때 자음의 개수와 모음의 개수를 출력하는 프로그램을 작성하세요.

while=input("영어 단어 입력:")
vowels=0
consonants=0
for char in word:
    if char in 'aeiouAEIOU':
        vowels+=1
    else:
        consonants+=1
print("입력한 단어 :", word)
print("모음 수 :", vowels)