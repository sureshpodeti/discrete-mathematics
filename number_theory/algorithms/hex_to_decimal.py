'''
  0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F
  A = 10 , B = 11, C = 12, D = 13, E = 14, F = 15
'''
def hex_to_decimal(h):
  d = {'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15, '0':0, '1':1,
       '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9
      }
  result = 0
  j = 0
  for i in range(len(h)-1, -1, -1):
    result += d[h[i]]*(16**j)
    j += 1

  return result 

h = raw_input()
print "decimal repr. of {} is :{}".format(h, hex_to_decimal(h))
