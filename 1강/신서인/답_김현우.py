#문자열을 입력받아, 해당 문자열에서 각 알파벳의 등장횟수를 세는 프로그램을 작성하세요

text = input("문자열 입력: ").lower()

for char in text:
    if char.isalpha():
        char_count[char] = char_count.get(char, 0) + 1

for char in sorted(char_count):
    print(f"'{char}': {char_count[char]}번")