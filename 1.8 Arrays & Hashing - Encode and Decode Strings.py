my_list = ["lint","code","love","you"]

def encode(my_list):
    result = ''
    for item in my_list:
        result += f'{item}:;' 
    return result

def decode(my_list):
    result = []
    word = ''
    for i in range(len(my_list)):
        if my_list[i] == ':' and my_list[i + 1] == ';':
            result.append(word)
            word = ''

        #Since the separator is made of 2 symbols, the following lines
        #ensures one of them doesn't make it into the decoded string
        elif my_list[i] == ';' and my_list[i - 1] == ':':
            pass

        else:
            word += my_list[i]

    return result

encoded_string = encode(my_list)
print(encoded_string)

decoded_string = decode(encoded_string)
print(decoded_string)
