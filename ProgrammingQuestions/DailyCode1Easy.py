#Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
def naive(lst, k):
    for i in range(0, len(lst)):
        for j in range(0, len(lst)):
            if i == j: continue
            if lst[i] + lst[j] == k: 
                return True
    return False
    
    
#Follow Up, One pass solution (Ignoring sorting)
def sorted_method(lst, k):
    sorted_lst = sorted(lst)
    i, j= 0, len(sorted_lst)-1
    while i < j:
        sum = sorted_lst[i] + sorted_lst[j]
        if sum < k: i+= 1
        elif sum > k: j += -1
        else: return True
    return False
        
    
if __name__ == "__main__":
    lst = [3, 4, 7, -1, 12]
    k = 16
    
    print("Naive  " + str(naive(lst, k)))
    print("Sorted " + str(sorted_method(lst, k)))