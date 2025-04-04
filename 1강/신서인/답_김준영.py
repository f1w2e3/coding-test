user_input = input()

user_input = user_input.lower()
filtered_input = [ch for ch in user_input if ch.isalpha()]

#중복제거
unique_chars = sorted(set(filtered_input))


for ch in unique_chars:
    print(f"{ch}: {filtered_input.count(ch)}")