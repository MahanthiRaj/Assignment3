from multiprocessing import Process
from memory_profiler import profile

def cube(n):
    print(n ** 3)

@profile
def main():
    
    for i in range(1, 101):
        p = Process(target=cube, args=(i,))
        p.start()
        p.join()

if __name__ == '__main__':
    main()