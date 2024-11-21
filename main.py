import build.Release.my_module as my_module
# import the time module
import time

# get the current time in seconds since the epoch
start_time = time.time()

def fib(n):
    if(n<=1):
        return n
    else:
        return fib(n-1) + fib(n-2)

print(fib(40))

curent_time = time.time()
py_time = curent_time - start_time
print(py_time)
start_time = time.time()

print(my_module.fib(40))

curent_time = time.time()
c_time = curent_time - start_time
print(c_time)

print()
print(c_time/py_time)

print(my_module.add(1, 2))