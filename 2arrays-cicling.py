import random
import math

#generate a random list
list = []
i=0
for i in range(0, 15):
    list.append(i)
    if len(list) == 15:
        random.shuffle(list)
        print(list)


def solution(A, K):
    """pre: recieves an array an a number K"""
    #  pos: returns an array cycled K times
    while K > 0:    
        A = A[-1:] + A[:-1]
        K -=1
    return A



solution(list, 1)
