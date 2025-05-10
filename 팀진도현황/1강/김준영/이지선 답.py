#문제 1
n = input("입력: ")
sum_digits = 0
for digit in n:
    sum_digits += int(digit)
print("출력: ", sum_digits)

#문제 2
word = input("입력: ")
vowel_count = 0
consonant_count = 0
for ch in word:
    if ch in vowels:
        vowel_count += 1
    else:
        consonant_count += 1
print(f"자음:{consonant_count} 모음:{vowel_count}")