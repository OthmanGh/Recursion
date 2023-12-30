# input : 12
# output : 1100

# input : 270
# output : 100001110


def convert_to_binary(number, result):
    if number // 2 == 0:
        return str(number % 2) + result
    
    result = str(number % 2) + result
    return convert_to_binary(number // 2, result)


print(convert_to_binary(270, ''))


