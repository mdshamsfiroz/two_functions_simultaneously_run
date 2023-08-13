#Run the two function simuntaneously
import threading
import time
def function1():
    while True:
        print("aaaaaa")
        time.sleep(1)
def function2():
    while True:
        print("bbbbbb")
        time.sleep(1)
thread1 = threading.Thread(target=function1)
thread1.start()
thread2=threading.Thread(target=function2)
thread2.start()
