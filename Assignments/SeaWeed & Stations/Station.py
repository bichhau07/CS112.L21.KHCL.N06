from sys import maxsize

def maxSubArraySum(a,size):
 
    max_so_far = -maxsize - 1
    max_ending_here = 0
    start = 0
    end = 0
    s = 0
 
    for i in range(0,size):
 
        max_ending_here += a[i]
 
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
            start = s
            end = i
 
        if max_ending_here < 0:
            max_ending_here = 0
            s = i+1
    print("{} {} {}".format(start + 1, end + 1, max_so_far))

def max_subarray(numbers):

    best_sum = 0  
    best_start = best_end = 0  
    current_sum = 0
    for current_end, x in enumerate(numbers):
        if current_sum <= 0:
            current_start = current_end
            current_sum = x

        else:
            current_sum += x

        if current_sum > best_sum:
            best_sum = current_sum
            best_start = current_start + 1
            best_end = current_end + 1  

    print("{} {} {}".format(best_start, best_end, best_sum))

n = int(input())
A = list(map(int,input().split()))

maxSubArraySum(A,len(A))
