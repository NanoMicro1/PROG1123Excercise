import random

count_on_board = 0 

for i in range(1,51):
    for j in range(5, 50):
        random_required_time = random.randint(5, 50)
    print(f"{i}번째 손님,", f"소요시간{random_required_time}")

    if 5 <= random_required_time <= 15:
        count_on_board = count_on_board + 1
    
print("Total amout of passenger that on borad is " f"{count_on_board}")