# Многопоточность - не работает пример для Windows
import multiprocessing as mp
import os

def do_this(what):
    whoami(what)

def whoami(what):
    print('Process %s says: %s' % (os.getpid(), what))

if __name__ == '__main__':
    whoami("I'am the main program")
    for n in range(4):
        p = mp.Process(target=do_this, args=("I'am function %s" % n,))
        p.start()


# Example with dishes on Threading