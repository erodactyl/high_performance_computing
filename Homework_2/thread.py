import queue as Queue, threading, os
import shutil
import time

fileQueue = Queue.Queue()
source = './source/'
dest = './dest/'

class ThreadedCopy:
  totalFiles = 0
  copyCount = 0
  lock = threading.Lock()

  def __init__(self):
    fileList = os.listdir(source)

    if not os.path.exists(dest):
      os.mkdir(dest)

    self.totalFiles = len(fileList)
    self.threadWorkerCopy(fileList)


  def CopyWorker(self):
    while True:
      fileName = fileQueue.get()
      shutil.copy(fileName, dest)
      fileQueue.task_done()
      with self.lock:
        self.copyCount += 1
        percent = (self.copyCount * 100) / self.totalFiles

  def threadWorkerCopy(self, fileNameList):
    for i in range(6):
      t = threading.Thread(target=self.CopyWorker)
      t.daemon = True
      t.start()
    for fileName in fileNameList:
      fileQueue.put(source + fileName)
    fileQueue.join()

initTime = time.perf_counter()
ThreadedCopy()
print(time.perf_counter() - initTime)