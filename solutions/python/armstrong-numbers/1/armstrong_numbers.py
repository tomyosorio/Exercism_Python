def is_armstrong_number(number):
    temp = number
    count = 0
    sum = 0
    isArmstrong = False

    while temp > 0:
        temp //= 10
        count += 1

    temp = number
    
    while temp > 0:
        sum += (temp % 10) ** count
        temp = temp // 10

    if sum == number:
        isArmstrong = True
    
    return isArmstrong