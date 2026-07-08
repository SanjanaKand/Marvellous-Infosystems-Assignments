'''
Design a Python application where multiple threads update a shared variable.

Use a Lock to avoid race conditions.
Each thread should increment the shared counter multiple times.
Display the final value of the counter after all threads complete execution
'''

import threading

Counter = 0
Lock = threading.Lock()

def Increment():
    global Counter

    for i in range(100000):
        Lock.acquire()
        Counter = Counter + 1
        Lock.release()

def main():
    Thread1 = threading.Thread(target=Increment)
    Thread2 = threading.Thread(target=Increment)
    Thread3 = threading.Thread(target=Increment)

    Thread1.start()
    Thread2.start()
    Thread3.start()

    Thread1.join()
    Thread2.join()
    Thread3.join()

    print("Final Counter Value :", Counter)

if __name__ == "__main__":
    main()

'''
Counter = 0
          │
          ▼
Create Lock
          │
          ▼
Create 3 Threads
          │
          ▼
Thread 1  Thread 2  Thread 3
     │        │         │
     └────────┼─────────┘
              ▼
Each thread repeats 100000 times:
    Acquire Lock
          │
          ▼
Increment Counter
          │
          ▼
Release Lock
          │
          ▼
All threads finish
          │
          ▼
Main thread prints Counter



'''