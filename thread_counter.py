import threading
import time

class Counter:
  def __init__(self, count):
    self.count = count
    self.lock = threading.Lock()

  def get_next(self):
    self.lock.acquire()
    current_val = self.count
    if self.count > -1: self.count -= 1
    self.lock.release()
    return current_val


class Worker(threading.Thread):
  def __init__(self, id, counter):
    threading.Thread.__init__(self)
    self.counter = counter
    self.threadID = id

  def run(self):
    val = 1
    while val > -1:
      val = self.counter.get_next()
      print(f"Thread {self.threadID} got: {val}")
      time.sleep(0.1)



counter = Counter(20)
threads = []

for i in range(1,4):
  t = Worker(i, counter)
  t.start()
  threads.append(t)


for t in threads:
  t.join()

print("Exit main")
