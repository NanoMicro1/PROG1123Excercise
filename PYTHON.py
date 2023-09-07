import random

online_meeting = random.sample(range(4, 28), 3)
print("Online meeting is", online_meeting)

available_numbers = []
for x in range(4, 28):
    if x not in online_meeting:
        available_numbers.append(x)

offline_meeting = random.sample(available_numbers, 1)
print("Offline meeting day is" , offline_meeting)
#내가 짠 코드 ↥

#=====================================================

#파이썬 강의가 짠 코드 ↘
from random import *
date = randint(4,28)
print("Offline meeting day is" , date)