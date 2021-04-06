import math
import timeit

start = timeit.default_timer()
# checking for prime
def is_prime(n):
   # checking for less than 1
   if n <= 1:
      return False
   # checking for 2
   elif n == 2:
      return True
   elif n > 2 and n % 2 == 0:
      return False
   else:
      # iterating loop till square root of n
      for i in range(3, int(math.sqrt(n)) + 1, 2):
         # checking for factor
         if n % i == 0:
            # return False
            return False
      # returning True
      return True

for y in range(1,1000000):
    if is_prime(y) == True:
        print(y)
            
 



#Your statements here

stop = timeit.default_timer()

print('Time: ', stop - start)        

        