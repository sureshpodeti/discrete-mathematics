'''
 Tower of Hanoi: 
  We have three towers labelled A,B,C, and n disks (with hole at the center) on tower A. The disk having small
  size placed above the bigger one. Our task is to move all disks from tower A to tower C using intermedite disk B.
  we are allowed move only one disk at a time.
 
  Algorithm:
    First move nth disk from A to B
    move (n-1) disks from A to C
    move nth disk from B to C
  
  Analysis:
    time complexicity analysis:
      recurrence relation: T(n) = 2T(n-1) + c
         n                                 n 
   n-1           n-1                       2(n-1)
n-2    n-2  n-2      n-2                   4(n-2)
                                           8(n-3)
.
.
1 1     ........
 --------------------------------------------------
                                       k=n
     total no.of operations             ∑ 2^k(n-k) 
                                       k=1 
 --------------------------------------------------
       = ( n+2n+4n+ ....) - (2+8+24+ ...)
                        n
       = [2^(n+1) -1] - ∑  2^i * i
                        i =1
      time complexicy: O(2^n)


space complexicity : O(n)
  
 mathematical anayslis:
   Let f(n) gives the minimum no.of moves needed to shift n disks from A to C, using rules specified
    f(1)=1, f(2) = 3 , f(3) = 7, f(4) = 15 ..
    By, looking at the pattern one can formaulate f(n) = 2^n -1 
   
'''




def tower_of_hanoi(A, B, C, n):
 if n == 1:
  print A +"-to-"+C 
  return 
 tower_of_hanoi(A,C,B,n-1)
 print A+"-to-"+C
 tower_of_hanoi(B, A, C, n-1) 



tower_of_hanoi("A", "B","C", 10)
