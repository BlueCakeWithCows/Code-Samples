#Good morning! Here's your coding interview problem for today.
#This problem was asked by Airbnb.
#Given a list of words, find all pairs of unique indices such that the #concatenation of the two words is a palindrome.
#For example, given the list ["code", "edoc", "da", "d"], return [(0, 1), (1, 0), (2, 3)].

def is_palindrome(word):
    for i in range(0, len(word)//2):
        if word[i] != word[-(i+1)]:
            return False
    return True

def get_indices(lst):
    indices = []
    for i, x in enumerate(lst[:-1]):
        for j, y in enumerate(lst[i+1:]):
            if is_palindrome(x+y):
                indices.append((i, i+j + 1))
            if is_palindrome(y+x):
                indices.append((i+j+1, i))
    return indices
x = ["code", "edoc", "da", "d"]
print(get_indices(x))
