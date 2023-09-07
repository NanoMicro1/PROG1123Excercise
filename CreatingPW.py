# some internet address (example http://google.com)
# http://는 제외
# .com은 제외
# 그러면 google만 남지? 그걸 추출하는 기능 구현

# 남은 글자 중 첫 3자리 (ex : goo) + 글자갯수(6) + 글자내 'e'갯수 + 특수기호추가(?)

# user_input = input("What is the address?")
import random

URL = input()

if URL.startswith("http://"):
    URL = URL[7:]
if URL.endswith(".com"):
    URL = URL[:-4]
elif URL.endswith(".net"):
    URL = URL[:-4]
print(URL)

first_3_letters = URL[0:3]
print(first_3_letters)

letters = len(URL)
print(letters)

e_count = 'e'
start = 0
amount_of_e = URL.count(e_count, start)
print(amount_of_e)

special_chars = "!@#$%^&*()-_=+[]{}|;:',.<>?/`~"
random_char = random.choice(special_chars)

print(first_3_letters + str(letters) + str(amount_of_e) + random_char)