def pre_run(intcode):
    intcode[1] = 12
    intcode[2] = 2

    return intcode

def process_intcode(intcode):
    int_pointer = 0
    #processed_intcode = intcode
    for i in range(len(intcode)):
        i = int_pointer
        x = intcode[i + 1]
        y = intcode[i + 2]
        z = intcode[i + 3]

        if intcode[i] == 1:
            intcode[z] = x + y

        elif intcode[i] == 2:
            intcode[z] = x * y

        elif intcode[i] == 99:
            break
        int_pointer += 4

        print(len(intcode)+3)
        if int_pointer + 3 >= len(intcode):
            break

    return intcode
