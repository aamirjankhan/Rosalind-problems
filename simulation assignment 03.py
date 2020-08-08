import time
print("-----------------------------------------------------------------------------------------------------------------------")
print("fibonacci through a normal approach")
def febonacci(number, k=3):
    old, new = 1, 1
    for i in range(number- 1):
        new, old= old, old+ new
    return new*k
tic= time.process_time()
print(febonacci(int(input("pleasen enter any integer: "))))
toc= time.process_time()
print("time taken is: "+str((toc-tic)*100)+"ms")
print("-----------------------------------------------------------------------------------------------------------------------")
print("febonacci through recursion")
result= 0
def fib_recursion(num):
    if num==1 or num==2:
        result = 1
    else:
        result= fib_recursion(num- 1)+ fib_recursion(num- 2)
    return result
tic= time.process_time()
print(fib_recursion(int(input("pleasen enter any integer: "))))
toc= time.process_time()
print("time taken is: "+str((toc-tic)*1000)+"ms")
print("-----------------------------------------------------------------------------------------------------------------------")
print("fibonacci through Memoization")
def fib_2(num, memo):
    if memo[num] is not None:
        return memo[num]
    if num == 1 or num == 2:
        result = 1
    else:
        result = fib_2(num-1, memo) + fib_2(num-2, memo)
    memo[num] = result
    return result
def fib_memo(num):
    memo = [None] * (num + 1)
    return fib_2(num, memo)
tic= time.process_time()
print(fib_memo(int(input("pleasen enter any integer: "))))
toc= time.process_time()
print("time taken is: "+str((toc-tic)*1000)+"ms")
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
print("time taken is: "+str((toc-tic)*1000)+"ms")
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
print("-----------------------------------------------------------------------------------------------------------------------")
print("Rosalind Problems: Rabbits and Recurrence Relations")
print("rabit recursive")
def rabbit_recursive(months, offsprings):
    if months<2:
        return months
    else:
        return rabbit_recursive(months-1, offsprings)+ rabbit_recursive(months-2, offsprings)*offsprings
tic= time.process_time()
print(rabbit_recursive(int(input("pleasen enter months: ")), int(input("pleasen enter number of offsprings: "))))
toc= time.process_time()
print("time taken is: "+str((toc-tic)*1000)+"ms")
print("-----------------------------------------------------------------------------------------------------------------------")
print("Rosalind Problems: Rabbits and Recurrence Relations")
print("rabit iterative")
def rabbit_iterative(months, offsprings):
    parent_1, parent_2 = 1, 1
    parent = 1  # Just a place holder in case n is too small
    for _ in range(2, months):
        parent = parent_1 + parent_2*offsprings
        parent_2, parent_1 = parent_1, parent
    return parent
tic= time.process_time()
print(rabbit_iterative(int(input("pleasen enter months: ")), int(input("pleasen enter number of offsprings: "))))
toc= time.process_time()
print("time taken is: "+str((toc-tic)*1000)+"ms")
  
























    

