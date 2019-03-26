"""This problem was asked by Apple.

Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds."""
from threading import Thread
from time import sleep

def schedule(f, n):
    def helper():
        sleep(n/1000.0)
        f()
    
    Thread(target = helper).start()
     
    

if __name__ == "__main__":
    def test_func():
        print("Hello")
    def potato():
        print("teemo")
    schedule(test_func, 1200)
    schedule(potato, 1000)
    schedule(test_func, 1200)