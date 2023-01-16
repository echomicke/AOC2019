def process_intcode(intcode):
    intcode_arr = intcode[:]

    for i in range(0, len(intcode_arr), 4):
        if i + 3 >= len(intcode_arr):
            break

        x = intcode_arr[intcode_arr[i + 1]]
        y = intcode_arr[intcode_arr[i + 2]]
        z = intcode_arr[i + 3]

        if intcode_arr[i] == 1:
            intcode_arr[z] = x + y

        elif intcode_arr[i] == 2:
            intcode_arr[z] = x * y

        elif intcode_arr[i] == 99:
            break

    return intcode_arr

def find_Noun_verb(intcode, targetOutputt):
    result = 0
    for noun in range(100):
        for verb in range(100):
            intcode[1] = noun
            intcode[2] = verb
            output = process_intcode(intcode)

            if output[0] == targetOutputt:
                result = 100 * noun + verb
                break

        if output[0] == targetOutputt:
            break

    return result



input_file = open("day2_input")
intcode_input = input_file.read()
input_file.close()

intcode_input = intcode_input.split(',')
intcode_input = list(map(int, intcode_input))

results = find_Noun_verb(intcode_input, 19690720)
print(results)
