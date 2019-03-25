"""Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5. """

from collections import OrderedDict

def largest_sum(lst):
    table = [0] * (len(lst) + 2)
    for index in range(0, len(lst))[::-1]:
        value = lst[index]
        table[index] = max(table[index+1], value+table[index+2], table[index+2])
    return table[0]
     
 #Space Constant version
def largest_sum2(lst):
    current = 0 
    prev = 0
    for index in range(0, len(lst))[::-1]:
        value = lst[index]
        current, prev = max(current, value + prev, prev), current
    return current
     
    

if __name__ == "__main__":
    ex = [2, 4, 6, 2, 5]
    assert largest_sum(ex) == 13
    assert largest_sum([5,1, 1, 5]) == 10
    
    assert largest_sum2(ex) == 13
    assert largest_sum2([5,1, 1, 5]) == 10

        
        
        