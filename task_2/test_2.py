def solve(value):
    Letters = 0
    Digits = 0
    for i in value.upper():
        try:
            if i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                Letters += 1
            elif i in '0123456789':
                Digits += 1
            else:
                pass
        except ValueError:
            pass
    return Letters, Digits


if __name__ == '__main__':
    value = str(input('write a sentence:'))
    Letters, Digits = solve(value)
    print('Letters = {}\nDigits = {}'.format(Letters, Digits))
