def pre_run(intcode):
    intcode[1] = 12
    intcode[2] = 2

    return intcode

def process_intcode(intcode):
    int_pointer = 0
    #processed_intcode = intcode
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

def challange_setup(intcode):
    intcode = pre_run(intcode)
    results = process_intcode(intcode)

    return results


input_file = open("day2_input")
intcode_input = input_file.read()
input_file.close()

intcode_input = intcode_input.split(',')
intcode_input = list(map(int, intcode_input))

chr_results = challange_setup(intcode_input)
print(chr_results[0])
