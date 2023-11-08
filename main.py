def fib_recursive(n, counts):
    """
    Return the nth Fibonacci number. 
    counts is a list of n+1 elements, where counts[i] is incremented
    each time fib_recursive(i, counts) is called.
    """    
    
    if n == 0:
        counts[n] += 1
        return 0
    elif n == 1:
        counts[n] += 1
        return 1
    else:
        counts[n] += 1
        return fib_recursive(n - 1, counts) + fib_recursive(n - 2, counts)
    
    ###TODO
    
    

    
def fib_top_down(n, fibs):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n in fibs:
        return fibs[n]
    else:
        fibs_ntrack = fib_top_down(n - 1, fibs) + fib_top_down(n - 2, fibs)
        fibs[n] = fibs_ntrack
        return fibs_ntrack
    


def fib_bottom_up(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib_n = 1
        fib_prev = 0

        for i in range(2, n + 1):
            temp = fib_n
            fib_n = fib_n + fib_prev
            fib_prev = temp

        return fib_n




def fib_bottom_up_better(n):
    ###TODO
    pass
