"""
Given a stream of elements too large to store in memory, pick a random element from the stream with uniform probability.
Some quick googling gave me a method called resevoir sampling. 
"""

import random




"""Method basically determines probability next item in stream would be picked if length of stream is current length. It then rolls a die and assigns it if it is picked."""
def resevoir(stream):
    val = None
    for i, e in enumerate(stream): 
        if random.randint(0, i) == 0:
            val = i
    return val
        
    
    
    

def countdown_generator(num):
    while num >= 0:
        yield num
        num -= 1
        
"""Testing is if values look reasonable, technically could do a Chi-squared or other distribution test but this is just a demo"""
if __name__ == "__main__":
    size = 10
    bins = [0] * size
    trials = 10000
    for i in range(0, trials):
        bins[resevoir(countdown_generator(9))] += 1
    print(bins)
    