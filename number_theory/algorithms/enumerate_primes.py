#_*_ coding: utf-8 _*_
'''
  Enumeration of prime numbers:
  ----------------------------
    f(n) = #{p∈ P: p≤ n∈ N ∧ n is prime}
    Algorithm:
      1. Let X be the set of all numbers ≤n, X = {2,3,4,5,...,n}
      2. Let P be the set which collects prime numbers 
      3. pick each item x from the set X, and do the following
      4. check if x ≤ sqrt(n), then add set X to P and terminate
      5. else, add x to set P and continue
      5. repeat step 3

    time complexicity: O(n^2)
    space complexicity: O(n)
   
'''
import math
def enumerate_primes(n):
 if n < 2:
  return []
 X = [i for i in range(2, n+1)]
 P = []
 while True:
  if X[0] > math.sqrt(n):
   P.extend(X)
   break
  item = X.pop(0)
  P.append(item)
  for j in range(0, len(X)):
   if j<len(X) and (X[j] % item ==0):
    X.pop(j)
    j -= 1

 return P


n = int(raw_input())
print enumerate_primes(n)
