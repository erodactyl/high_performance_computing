import queue as Queue, multiprocessing, os
import shutil
import time

fileQueue = Queue.Queue()
source = './source/'
dest = './dest/'

class MultiProcessedCopy:
  totalFiles = 0
  copyCount = 0
  lock = multiprocessing.Lock()

  def __init__(self):
    fileList = os.listdir(source)

    if not os.path.exists(dest):
      os.mkdir(dest)

    self.totalFiles = len(fileList)
    self.processWorkerCopy(fileList)


  def CopyWorker(self, fileName):
    shutil.copy(source + fileName, dest)
    self.lock.acquire()
    self.copyCount += 1
    percent = (self.copyCount * 100) / self.totalFiles
    self.lock.release()

  def processWorkerCopy(self, fileNameList):
    pool = multiprocessing.Pool(6)
    pool.map(self.CopyWorker, fileNameList)
    pool.close()
    pool.join()

initTime = time.perf_counter()
MultiProcessedCopy()
print(time.perf_counter() - initTime)