def solve(a, b, c):
    count = 0
    result = []
    for i in range(a, b + 1):
        if i % c == 0:
            result.append(i)
            count += 1
        else:
            pass
    return count, result


if __name__ == '__main__':
    number_1 = int(input('write number1:'))
    number_2 = int(input('write number2:'))
    number_3 = int(input('write number3:'))
    count, result = solve(number_1, number_2, number_3)
    print(str(count) + ', because ' + str(result)[1:-1] + ' are divisible by ' + str(number_3))








