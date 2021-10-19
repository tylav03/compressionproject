# opens input_text.txt and assigns it to variable text
text_file = open("input_text.txt", "r")
text = text_file.read()

# takes in a single character and returns it as a binary string
def find_binary(p1:str) -> str:
    if p1 in " etarons":
        if p1 == " ":
            return "1000"
        elif p1 == "e":
            return "1001"
        elif p1 == "t":
            return "1010"
        elif p1 == "a":
            return "1011"
        elif p1 == "r":
            return "1100"
        elif p1 == "o":
            return "1101"
        elif p1 == "n":
            return "1110"
        elif p1 == "s":
            return "1111"
    else:
        ascii = ord(p1)
        binary = format(ascii, "b")
        while len(binary) < 8:
            binary = "0" + binary
        return binary

# takes in a whole string and returns a whole binary string
def text_to_binary(p1:str) -> str:
    output = ""
    for i in p1:
        output = output + find_binary(i)
    return output

# used for compression ratio only; takes in a whole string and doesnt compress, just outputs to binary
def all_binary(p1:str) -> str:
    output = ""
    for i in p1:
        ascii = ord(i)
        binary = format(ascii, "b")
        while len(binary) < 8:
            binary = "0" + binary
        output = output + binary
    return output

# opens binary.txt and writes p1 to it
def write_to_binary(p1: str):
    binary_file = open("binary.txt", "w")
    binary_file.write(p1)
    binary_file.close()

# opens binary.txt and returns its contents
def read_binary() -> str:
    binary_file = open("binary.txt", "r")
    p1 = binary_file.read()
    binary_file.close()
    return p1

# opens output.txt and returns its contents
def write_to_output(p1: str):
    output_file = open("output.txt", "w")
    output_file.write(p1)
    output_file.close()

# takes in a whole binary string and returns a whole text string
def binary_to_text(p1: str) -> str:
    char_list = []
    i = 0
    while i < len(p1):
        if p1[i] == "0":
            binary = p1[i:i+8]
            ascii = int(binary, 2)
            letter = chr(ascii)
            char_list.append(letter)
            i = i+8
        elif p1[i] == "1":
            binary = p1[i:i+4]
            if binary == "1000":
                char_list.append(" ")
            elif binary == "1001":
                char_list.append("e")
            elif binary == "1010":
                char_list.append("t")
            elif binary == "1011":
                char_list.append("a")
            elif binary == "1100":
                char_list.append("r")
            elif binary == "1101":
                char_list.append("o")
            elif binary == "1110":
                char_list.append("n")
            elif binary == "1111":
                char_list.append("s")
            i = i+4
    output = ""
    for i in char_list:
        output = output + i
    return output


# compression_ratio = 1-(len(text_to_binary(text)) / len(all_binary(text)))
# print(compression_ratio)

write_to_binary(text_to_binary(text))
write_to_output(binary_to_text(read_binary()))

