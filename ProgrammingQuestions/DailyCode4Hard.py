"""Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3."""

def func(input):

    #Task 1 is split negative (and zero) and positive numbers into different parts
    i, j = 0, len(input)-1
    positive_start = 0
    while i < j:
        if input[i] < 1:
            i += 1
        elif input[j] > 0:
            j += -1
        else:
            input[i], input[j] = input[j], input[i]
            i += 1
            j += -1
            positive_start = i
        
    #Observe that if any integers a are > length of input then by default the smallest integer is less than length of input
    highest_int = len(input) - positive_start
    
    
    #Task 2: Use indices and positive/ negative as markers for whether an integer is present (i.e. counting sort in place) 
    for i, value in enumerate(input[positive_start:]):
        if value <= highest_int: 
            input[value + positive_start -1 ] = -1 * abs(input[value + positive_start -1])
   
   #Task 3: Iterate through finding the smallest integer; also put the values back to positive
    min_integer = highest_int
    for i, value in enumerate(input[positive_start:]):
        if value > 0: 
            min_integer = min(min_integer, i)
        else:
            input[i + positive_start ] = abs(input[i + positive_start])
        
    #Task 4: Put the list ac
    #Account for zero index
    min_integer +=1 
    
    return min_integer

if __name__ == "__main__":
    input =  [3, 4, -1, 1]
    assert func(input) == 2
    input = [1,2, 0]
    assert func(input) == 3
    