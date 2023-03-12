import random
import time
n=1000000
l= [random.uniform(0, 1) for _ in range(n)]

start_time= time.time()
maximum=l[0]
for element in l:
    #print(element)
    if element>maximum: maximum=element
end_time=time.time()
print(f"il massimo e' {maximum}")
print(f"durata dell'algoritmo {end_time-start_time}")