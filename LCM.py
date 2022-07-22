def LCM(number1, number2):
    maximum = max(number1, number2)
    i = maximum
    while True:
        if (i % number1 == 0  and i % number2 == 0):
            lcm = i
            break
        i += maximum

    return lcm
print(LCM(120,140))
