#Aamir Jan Khan
#SP17-BSI-017
#Assignment Number 3
#Fibonacci series and Rabbit Recurrence problem from Rosalind
#Basically there are three ways by which we can code fibonacci series i.e.
#Recursion method: this is the most slow and a naaive approach with the time complexity of O(2n)
#Memoization method: this is e better approach from recursion in which we maintain a memo list and having time complexity of O(1)
#Bottoms up approach: this is a much better and advances approach of memoization in which the time complexity is reduced upto an extent
import time
print("-----------------------------------------------------------------------------------------------------------------------")
print("fibonacci through a bottoms up approach")
def fib_bottom_up(num):
    if num == 1 or num == 2:
        return 1
    bottom_up = [None] * (num+1)
    bottom_up[1] = 1
    bottom_up[2] = 1
    for i in range(3, num+1):
        bottom_up[i] = bottom_up[i-1] + bottom_up[i-2]
    return bottom_up[num]
tic= time.process_time()
print(fib_bottom_up(int(input("pleasen enter any integer: "))))
toc= time.process_time()
print("time taken is: "+str((toc-tic)*100)+"ms")
#Now we will use a similar approach to solve the Rabbit recurrence problem and will try to minimize the time complexity
#we will use the highest test case of months= 40 and offsprings= 5
print("-----------------------------------------------------------------------------------------------------------------------")
print("Rosalind Problems: Rabbits and Recurrence Relations")
def rabbit_recurrence(months, offsprings):
    parent, child= 1,1
    for i in range(months- 1):
        child, parent= parent, parent+ (child*offsprings)
    return child
tic= time.process_time()
print(rabbit_recurrence(int(input("pleasen enter months: ")), int(input("pleasen enter number of offsprings: "))))
toc= time.process_time()
print("time taken is: "+str((toc-tic)*1000)+"ms")
#Some other algorithms and their time complexity is mentoioned below i only used the best algorithm
#-----------------------------------------------------------------------------------------------------------------------
#fibonacci through a normal approach
#pleasen enter any integer: 35
#9227465
#time taken is: 0.0sec
#-----------------------------------------------------------------------------------------------------------------------
#febonacci through recursion
#pleasen enter any integer: 35
#9227465
#time taken is: 4.578125sec
#-----------------------------------------------------------------------------------------------------------------------
#fibonacci through Memoization
#pleasen enter any integer: 35
#9227465
#time taken is: 15.625ms
#-----------------------------------------------------------------------------------------------------------------------
#fibonacci through a bottoms up approach
#pleasen enter any integer: 35
#9227465
#time taken is: 0.03125sec
#-----------------------------------------------------------------------------------------------------------------------
#Some other algorithms and their time complexity is mentoioned below i only used the best algorithm
#Rosalind Problems: Rabbits and Recurrence Relations
#pleasen enter months: 40
#pleasen enter number of offsprings: 5
#148277527396903091
#time taken is: 0.0ms
#-----------------------------------------------------------------------------------------------------------------------
#Rosalind Problems: Rabbits and Recurrence Relations
#rabit recursive
#pleasen enter months: 40
#pleasen enter number of offsprings: 5
#148277527396903091
#time taken is: 79656.25ms
#-----------------------------------------------------------------------------------------------------------------------
#Rosalind Problems: Rabbits and Recurrence Relations
#rabit iterative
#pleasen enter months: 40
#pleasen enter number of offsprings: 5
#148277527396903091
#time taken is: 15.625ms
