# _*_ coding: utf-8 _*_

'''
  Decimal to binary conversion:
  ----------------------------
   Number theory application seen here, 
    we use reminder theorem( or division theorem)
     Theorem: ∀a,b,q,r ∈ Z, b ≠ 0 ∧ a ≥ b:  0 ≤ r< b → a = bq + r
     eg: n = 12 
        12 = 2*6 + 0 
         6 = 2*3 + 0
         3 = 2*1 + 1
         1 = 2*0 + 1
        so, (12)10 = (1100)2
    Algorithm:
      1. Let R be the set which stores the result
      2. if n == 1 or n == 0 then prepend n to R and terminate
      3. q = n /2 , r = n % 2, add r to R 
      4. n = q, and got to step 2  

  
'''
def binary_num(n, l):
 if n == 1 or n == 0:
  l.append(n)
  l.reverse()
  return l
 r = n % 2
 q = n/2
 l.append(r)
 return binary_num(q, l) 
 
  


n = int(raw_input())
l = []
print binary_num(n, l)
