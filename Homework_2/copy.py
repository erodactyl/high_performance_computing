import shutil
import os
import time

source = './source/'
dest = './dest/'

if not os.path.exists(dest):
  os.mkdir(dest)

files = os.listdir(source)

initTime = time.perf_counter()

for f in files:
  shutil.copy(source + f, dest)

print(time.perf_counter() - initTime)