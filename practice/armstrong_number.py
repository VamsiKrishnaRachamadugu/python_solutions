def is_armstrong(arm_num):
    length = len(str(arm_num))
    total = 0
    temp = arm_num
    for i in range(length):
        rem = int(arm_num) % 10
        total = int(total) + rem ** length
        arm_num = int(arm_num) / 10
    return temp == total


print(is_armstrong(1634))
