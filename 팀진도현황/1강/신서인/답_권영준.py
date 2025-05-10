#문제설명) 문자열을 입력받아, 해당 문자열에서 각 알파벳의 등장횟수를 세는 프로그램을 작성하세요.
#대소문자는 구분하지 않습니다.

#조건) 문자열에 포함된 알파벳에 대해 등장 횟수를 출력해야 합니다.
#결과는 알파벳 순서대로 출력해야 합니다.
#공백은 무시하고 알파벳만 고려합니다.

from collections import Counter
input_string = input("문자열을 입력하세요: ")

input_string = input_string.replace(" ", "")
count = Counter([char for char in input_string])

for char in sorted(count.keys()):
    print(f"{char}: {count[char]}")