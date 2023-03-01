import argparse
import time

t1 = time.time()

#Ascii Programing Language interpreter


parser = argparse.ArgumentParser(description='Ascii Programing Language interpreter')
parser.add_argument('file_path', help='path to the input file')
args = parser.parse_args()

file_path = args.file_path

global array, pointer

array_length = 1000
array = [0 for i in range(array_length)]
pointer = array_length // 2


def commands(char):
    global array, pointer
    
    def print_all():
        str_out = ""
        for val in array:
            if val != 0:
                str_out += chr(val)
        print(str_out)

    def hold():
        print("")
        input("Press enter to continue")
    
    match char:
        case "+": array[pointer] += 1
        case "-": array[pointer] -= 1
        case "r": array[pointer] = 0
        case "p": print(array[pointer])
        case "c": print(chr(array[pointer]), end='')
        case ">": pointer += 1
        case "<": pointer -= 1
        case "i": array[pointer] = int(input())
        case "s": array[pointer] = ord(input()[0])
        case "a": print_all()
        case "h": hold()



def complex_command(commands):
    commands = "".join(commands).replace("[", "").replace("]", "").split(",")
    #takes a array, where the first element is the command and the rest are the arguments
    cmd = commands[0]
    
    def f(commands):
        search = commands[1]
        #find the first occurence of search in the array
        for i in range(pointer, len(array)):
            if array[i] == search:
                pointer = i
                break
    
    def b(commands):
        pointer = commands[1]

    def l(commands):
        #interpret commands[1] as roman numerals
        in_str = commands[1]
        roman_to_int_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        result = 0
        prev_value = 0

        for c in in_str[::-1]:
            value = roman_to_int_map[c]
            if value > prev_value:
                result += value - 2 * prev_value
            else:
                result += value
            prev_value = value

        return result
    
    def o(commands):
        array[pointer] = ord(commands[1])

    def k(commands):
        for i in range(int(commands[2])):
            run(commands[1])

    def j(commands):
        return int(commands[1]) if array[pointer] != 0 else None
    
    match cmd:
        case "f": f(commands) #find
        case "b": b(commands) #pointer to commands[1]
        case "l": l(commands) #interpret commands[1] as roman numerals
        case "o": o(commands) #ord
        case "k": k(commands) #loop commands[1] commands[2] times
        case "j": return j(commands) #jump to commands[1] char index in the input string if array[pointer] != 0


str_input = open(file_path, "r").read()

def run(str_input):
    command_queue = []
    i = 0
    while True:
        if i >= len(str_input):
            break
        char = str_input[i]
        if char == "[":
            command_queue.append(char)
        elif char == "]":
            command_queue.append(char)
            return_val = complex_command(command_queue)
            if return_val != None:
                i = return_val
            command_queue = []
        elif command_queue != []:
            command_queue.append(char)
        elif char in "+-><rpcisah":
            commands(char)
        else:
            print("Invalid command: " + char)
        i += 1

if __name__ == "__main__":
    run(str_input)
    print("\nexecution time: " + str(int((time.time() - t1)*1000)) + "ms")