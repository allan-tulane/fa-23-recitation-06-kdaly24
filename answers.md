# CMPS 2200 Recitation 06
## Answers

**Name:**_______Killian Daly___________
**Name:**_________________________


Place all written answers from `recitation-07.md` here for easier grading.



- **2)**
$W(n) = W(n-1) + W(n-2) + 1$

This recursion can be solved, and is leaf dominated. This can be simplified to $O(2^n)$

- **3)**
$W(n) = W(n-1) + 1$

This can be solved as $O(n)$ 

- **4)**
Due to the fact that n-1 iterates as well as n-2, the counts list shows us that many values in the fibonacci sequence are calculated twice, once from the W(n-1) branch and once from W(n-2)

- **6)**
In the new algorithm, each fib_town_down(i) in the fibonacci sequence is called once as the list of fibs[n] keeps the previous used top down values, and potentially referenced again when its same fib[n] value is found. 
With that, our Work is different, and can be reduced to W(n) as O(n). Span is the same, S(n) as O(n)

- **8)**
N times, as bottom up extends from 0 to n. With this in mind, work and span of Fib Bottom Up are $W(n)$ as $O(n)$ and $S(n)$ as $O(n)$
