# String Reversal : 
#? input : the simple engineer
#? output : reenigne elppmis eht

def stringReversal(input):
    if not input:
        return '';

    return stringReversal(input[1:]) + input[0];


print(stringReversal('the simple engineer'))
