import threading, queue
import time


def do_this(what):
    whoami(what)

def whoami(what):
    print('Thread %s says: %s' % (threading.current_thread(), what))

if __name__ == '__main__':
    whoami("I'am the main program")
    for n in range(4):
        p = threading.Thread(target=do_this,
            args=("I'am function %s" % n,))
        p.start()



# Example with dishes
def washer(dishes, dish_queue):
    for dish in dishes:
        print('Washing', dish,'dish')
        time.sleep(5)
        dish_queue.put(dish)

def dryer(dish_queue):
    while True:
        dish = dish_queue.get()
        print('Drying', dish,'dish')
        time.sleep(10)
        dish_queue.task_done()

dish_queue = queue.Queue()
for n in range(2):
    dryer_thread = threading.Thread(target=dryer, args=(dish_queue,))
    dryer_thread.start()
dishes = ['salad', 'bread', 'entree', 'dessert']
washer(dishes, dish_queue)
dish_queue.join()