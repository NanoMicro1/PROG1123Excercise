# def std_weight():
#     data = int(input())
#     ave_weight = (data - 95) * 0.6
#     print(f"2번째{ave_weight:.2f}")
    
# std_weight()

def std_weight(height, gender):
    if gender == "남자":
        return height * height * 22
    else :
        return height * height * 21

height = 175
gender = "남자"
weight = round(std_weight(height / 100, gender), 2)

print("키 {0}cm {1}의 표준 체중은 {2}kg입니다".format(height,gender,weight))
