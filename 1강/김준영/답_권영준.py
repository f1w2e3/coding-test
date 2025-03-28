#문제1: 그리디 알고리즘
#어떤 수 N이 주어졌을때 N의 모든 자릿수의 합을 구하는 프로그램을 작성하세요.
#예시) 
#입력: 12394
#출력: 19

N = input("숫자를 입력하세요: ")

sum_of_digits = sum(int(digit) for digit in N)

print(f"자릿수의 합: {sum_of_digits}")



#문제2: 구현
#어떤 영어 단어를 입력했을때 자음의 개수와 모음의 개수를 출력하는 프로그램을 작성하세요.
#예시)
#입력: airplane
#출력: 자음:4 모음:4

word = input("영어 단어를 입력하세요: ")

vowels = "aeiouAEIOU"
vowel_count = 0
consonant_count = 0

for char in word:
    if char.isalpha():
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

print(f"모음의 개수: {vowel_count}")
print(f"자음의 개수: {consonant_count}")