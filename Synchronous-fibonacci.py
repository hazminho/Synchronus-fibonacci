import concurrent.futures
import time
import math
def matematika(x):
 n = int(math.sqrt(x))
 return n*n == x
def find_fibonacci(n):
 
 return matematika(5*n*n + 4) or matematika(5*n*n - 4)


def do_something(x):
  for i in range(100):
    if (find_fibonacci(i) == True):
      print(i,"adalah sebuah angka fibonacci")
      time.sleep(1)
    else:
      print(i,"BUKAN sebuah angka fibonacci ")
      


start = time.perf_counter()

for i in range(5):
  do_something(1)

finish = time.perf_counter()

executed_time = round(finish - start, 2)
print(f"Finished in {executed_time} second(s)")
