# HPC Homework 2

## Setup
```bash
cd source
dd if=/dev/zero of=filename.txt count=1024000 size=1024
cp filename.txt filename2.txt
cp filename.txt filename3.txt
cp filename.txt filename4.txt
```

## Running
```bash
python3 copy.py
python3 thread.py
python3 process.py
```

Delete dest folder after running every time

copy.py ran in 8.287555631 seconds, thread.py ran in 5.627334852000001 seconds, and processes.py ran in 4.254924563 seconds for 4 files each with 1GB size.