#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'countMinimumOperations' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countMinimumOperations(arr):
    # Write your code here
    '''
    Given a list which is a permutation of the seuqnece [1,2,3 ... , n]
    Goal to transform this list into the order sequence from 1 to n, using the minimum possible number of operations
    
    Two types of operations:
        1. Shifting the array cyclically by 1 towards the left
        2. Swapping any 2 elements of the array
        
    However, once 2 is performed, operations cannot be performed again.
    Once we swap any two elements, we can't go back and do operation 1 (SO CAN'T GO BACK AND DO AT ALL). (VERY LIMITING / SIMPLIFIES THE SOLUTION). 
    
    So need to sort array, using just the two operations allowed. shifting array 1 position left, swwapping any two elements of the array.
        How to tackle the algorithm?
            Can find operations that can be performend independently
    
    Consider early exit for n = 1 (solution would be 0 in this scenario)
    2nd constraint useful as don't have to do pre-checks
    
    Remmeber that even if operation available, mightn't need be performed
    
    Can only perform operation 1 from 0 up to n-1 times (so we can run this)
        Same with operation 2, can only do it from 0 up to n-1 times
    
    If we do the 1st cycle of shifting array without swapping values, will this be sorted? no
        Then swap x number of times
    Max number of operations = n, as swapping elements will get this
    Always just need to compare that number of operations <= current solution
    '''
    n = len(arr) # Gives us the number of elements in our array
    if n == 1:
        return 0 # Early exit, as if there's only one element we know it's already sorted correctly
    
    number_of_operations = n # Like you said during our session, this is the worst-case answer if we were to sort things just by swaps.
    
    def operation_1(current_arr): # Operation for performing the cyclical shift one to the left (rotating everything left by one position)
        # arr = [5, 1, 2, 3, 4]
        shifted_array = current_arr[1:] + [current_arr[0]] # Syntax you added in, far more efficient way to do so than how I was intiially planning to do it (for-loop)
        # arr = [1, 2, 3, 4, 5]
        return shifted_array # From this function we return the list that has been shifted
    
    def operation_2(current_arr): # Operation for counting the minimum number of swaps needed for sorting
        
        visited = [False] * n # Create this list which tracks if index i has been included in a cycle yet
        swaps = 0 # This is the running total of minimum swaps needed (we update as we go through the for-loop)
        
        for i in range(n): # Loop through every index of the list
            #
            if visited[i] or current_arr[i] == i+1: # If we already visited this index, or it's in the right position (e.g at index 2 we want the number to be 3)
                continue # We can continue to the next one in that case
            cycle_length = 0 # This is used for measuring the length of a single cycle
            j = i # We only need to start following the cycle from the i currently being looked at in our for-loop
            while not visited[j]:
                visited[j] = True # Mark the index as visited so we don’t process it again in another cycle
                j = current_arr[j] - 1 # Move to the index where the current value should be placed (Since values are from 1 to n, value x should go at index (x-1))
                cycle_length += 1 # Increase the size of the current cycle by 1

            swaps += cycle_length - 1 # A cycle of length K will need K-1 swaps to place all elements correctly

        return swaps   # We return this minimum number of swaps for sorting
    

    current_arr = arr[:] # Just making a copy of the array so not to affect the input
    
    
    for shifts_used in range(n): # Trying each number of shifts, so 0 shifts, 1 shift, 2 shifts, all the way to n-1 left shifts
        swaps_needed = operation_2(current_arr) # Number of swaps needed to sort is simply gotten from our operation_2 function
        total_operations = shifts_used + swaps_needed # The total cost = shifts (done first) + swaps still needed (done second)

        if total_operations < number_of_operations: # Check if this total_operations value is smallest answer seen so far
            number_of_operations = total_operations # If smallest, we update number_of_operations to be this new smallest number of operations seen so far

        current_arr = operation_1(current_arr) # We move onto the next rotation in the for-loop and repeat this

    return number_of_operations # We can now get and return a minimum number of operations for this question
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = countMinimumOperations(arr)

    fptr.write(str(result) + '\n')

    fptr.close()