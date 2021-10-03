import time
import threading
from Queue import Queue

que = Queue()

orders = ['pizza','samosa','pasta','biryani','burger']

def place_order(orders):
    for order in orders:
        que.enqueue(order)
        print("Order enqued:",order)
        time.sleep(0.5)

def serve_order(orders):
    time.sleep(1)
    while not que.is_empty():
        a = que.dequeue()
        print("Order Served:",a)
        time.sleep(2)

t1 = threading.Thread(target=place_order, args=(orders,))
t2 = threading.Thread(target=serve_order, args=(orders,))

t1.start()
# time.sleep(1)
t2.start()

t1.join()
t2.join()
print()
print("Order been Served !!!")
