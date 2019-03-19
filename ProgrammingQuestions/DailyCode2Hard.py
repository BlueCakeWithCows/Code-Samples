#Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
from operator import mul
from functools import reduce

def func(lst):
    product = reduce(mul, lst, 1)
    new_lst = [0] * len(lst)
    
    for i, value in enumerate(lst):
        new_lst[i] = product / value
    
    return new_lst
    
    
#Do the same without the division operator
def without_division(lst):
    #For any integer i the number is [a[0] * ... * a[i-1]  * a[i+1] * ... a[l-1]]
    #We can precompute the left and right side for all numbers in linear time and then multiply the left and right half to form the new array
    n = len(lst)
    left_arr, right_arr = [0] * n, [0] * n
    left_arr[0] = lst[0]
    right_arr[n-1] = lst[n-1]
    for i in range(1, n):
        left_arr[i] = left_arr[i-1] * lst[i]
        right_arr[n - 1 - i] = right_arr[n-i] * lst[n-1- i]
        
    new_lst = [0] * n
    new_lst[0] = right_arr[1]
    new_lst[n-1] = left_arr[n-2]
    
    for i in range(1, n-1):
        new_lst[i] = left_arr[i-1] * right_arr[i+1]
    return new_lst
        
    
    
if __name__ == "__main__":
    #[1, 2, 3, 4, 5] should be  [120, 60, 40, 30, 24]
    lst = [1, 2, 3, 4, 5]
    
    print("Result of [1, 2, 3, 4, 5]  " + str(func(lst)))
    print("Result of [1, 2, 3, 4, 5]  " + str(without_division(lst)))