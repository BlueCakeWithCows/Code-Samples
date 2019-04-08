"""You run an e-commerce website and want to record the last N order ids in a log. Implement a data structure to accomplish this, with the following API:

record(order_id): adds the order_id to the log
get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N."""


from collections import deque

class Log:
    def __init__(self, N):
        self.__store = deque(maxlen = N)
        
    def record(self, order_id):
        if len(self.__store) == self.__store.maxlen:
            self.__store.popleft()
        self.__store.append(order_id)
        
    """Note, get_last(1) will return last item stored. get_last(0) will return None."""
    def get_last(self, i):
        if len(self.__store) < i or i < 1: 
            return None;
        return self.__store[len(self.__store) - i]
    
if __name__ == "__main__":
    records = Log(3)
    records.record(32)
    records.record(15)
    records.record(12)
    records.record(19)
    assert(records.get_last(3) == 15)
    assert(records.get_last(1) == 19)