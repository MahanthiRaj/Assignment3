from multiprocessing import Process
from memory_profiler import profile

@profile
def square(n):
    print (n * n)
    

if __name__ == "__main__":
    p = Process(target=square, args=(5,))
    p.start()
    p.join()
