def solution(price, money, count):
    sum = 0
    for i in range(1, count + 1):
        sum += i * price

    answer = sum - money

    if answer < 0:
        return 0

    return answer
print(solution(3,20,4))