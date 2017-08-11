# _*_ coding: utf-8 _*_
'''
  Program to find gcd(a,b):
   Algorithm:
    1. a==b → return a
    2. a ==0 ∧ ¬b==0 →  return b
    3. b == 0 ∧ ¬a==0 →  return a 
    4. a>b →  swap a and b
    5. q = b/a ∧ r = b -a*q
    6. recursively call gcd(a, r)

  time complexicity: O(n)
  space compleixity: O(1) 
'''
def gcd(a,b):
 if a == b:
  return a
 if a==0 and not b==0:
  return b
 if b ==0 and not a==0:
  return a
 
 if a>b:
  c = a
  a = b
  b =c
 
 q = b/a
 r = b - a*q
 return gcd(a,r)


a, b = raw_input().split(" ")
a = int(a)
b = int(b)
print gcd(a,b)
