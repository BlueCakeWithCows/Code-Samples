"""The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.

Hint: The basic equation of a circle is x2 + y2 = r2."""

import random

def monte_carlo_guess():
    hits = 0
    trials = 0.0
    estimate = 0.0
    delta = 1
    sigma = 1.0
    
    precision = 0.0005**2
    while sigma * 4> precision or trials <1000:
        if trials%100000 == 0:
            print("Trial {} at {}".format(trials, sigma))
        trials += 1
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x**2 + y**2 <= 1:
            hits +=1 

        sigma = (trials * (hits/trials) * (1.0- hits/trials))
        sigma = sigma/(trials**2)
       
    estimate = 4.0  * (hits/trials)
    print("Took {} to estimate {} at 2 SD confidence (~95% confidence) ".format(trials,round(estimate,3)))
    return round(estimate, 3)
          
        

if __name__ == "__main__":
    print(monte_carlo_guess())
    