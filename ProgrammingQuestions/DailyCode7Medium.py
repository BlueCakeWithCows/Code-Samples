 #Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.
from collections import OrderedDict

def get_mappings(codes, string):
    table = [0] * (1 + len(string))
    table[len(string)] = 1
    
    for index in range(0, len(string))[::-1]:
        total = 0
        substring = string[index:]
        for code in codes:
            if substring.startswith(code):
                total += table[index + len(code)]
                
        table[index] = total
    return table[0]

if __name__ == "__main__":
    letter_to_code = {'a': 1, 'c': 3, 'b': 2, 'e': 5, 'd': 4, 'g': 7, 'f': 6, 'i': 9, 'h': 8, 'k': 11, 'j': 10, 'm': 13, 'l': 12, 'o': 15, 'n': 14, 'q': 17, 'p': 16, 's': 19, 'r': 18, 'u': 21, 't': 20, 'w': 23, 'v': 22, 'y': 25, 'x': 24, 'z': 26}
    codes = OrderedDict((str(ch), idx) for idx, ch in letter_to_code.items())
    assert get_mappings(codes, '111') == 3


        
        
        