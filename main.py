# Brainf*ck interpreter
print("Brainfuck interpreter")
print("(c) Rahul Wavare 2022")
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("filename", help="Brainfuck file to interpret")
args = parser.parse_args()


def isascii(s):
    """Check if the characters in string s are in ASCII, U+0-U+7F."""
    return len(s) == len(s.encode())


print(f"Reading program... ({args.filename})")
try:
    with open(args.filename) as f:
        program = f.read()
except:
    print("error opening file")
    quit()
inst_pointer = 0
mem_bytes = 30000

print(f"Initializing memory... ({mem_bytes} bytes) \n")
array = [0 for _ in range(mem_bytes)]
pointer = 0

while True:
    i = program[inst_pointer]
    # print(f"instruction: {i}, char {inst_pointer}, current cell value: {array[pointer]}")
    if i == ">":
        pointer += 1
        if pointer > mem_bytes - 1:
            pointer -= mem_bytes
    elif i == "<":
        pointer -= 1
        if pointer < 0:
            pointer += mem_bytes
    elif i == "+":
        array[pointer] += 1
        if array[pointer] > 255:
            array[pointer] -= 256
    elif i == "-":
        array[pointer] -= 1
        if array[pointer] < 0:
            array[pointer] += 256
    elif i == ".":
        print(chr(array[pointer]), end="")
    elif i == ",":
        while True:
            char = input("")
            if not (len(char) == 1 and isascii(char)):
                continue
            break
        array[pointer] = ord(char)
    elif i == "[":
        if array[pointer] == 0:
            j = inst_pointer
            k = 1
            while True:
                j += 1
                if program[j] == "[":
                    k += 1
                elif program[j] == "]":
                    k -= 1
                if k == 0:
                    inst_pointer = j + 1
                    break
    elif i == "]":
        if array[pointer] != 0:
            j = inst_pointer
            k = 1
            while True:
                j -= 1
                if program[j] == "]":
                    k += 1
                elif program[j] == "[":
                    k -= 1
                if k == 0:
                    inst_pointer = j
                    break

    inst_pointer += 1
    if inst_pointer >= len(program):
        break
