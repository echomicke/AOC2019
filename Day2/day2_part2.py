def process_intcode(intcode):
    for i in range(0, len(intcode), 4):
        if i + 3 >= len(intcode):
            break

        x = intcode[intcode[i + 1]]
        y = intcode[intcode[i + 2]]
        z = intcode[i + 3]

        if intcode[i] == 1:
            intcode[z] = x + y

        elif intcode[i] == 2:
            intcode[z] = x * y

        elif intcode[i] == 99:
            break

    return intcode
