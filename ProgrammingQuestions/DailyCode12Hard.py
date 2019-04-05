"""There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:"""


def waysToClimb(n, steps):
    table = [0] * (n+1)
    table[n] = 1
    for i in reversed(range(n)):
        table[i] = sum([table[i + k] for k in steps if i+k < n+1])
    return table[0]
        

if __name__ == "__main__":
    assert waysToClimb(4, [1,2]) == 5
    assert waysToClimb(4, [1,2,4]) == 6