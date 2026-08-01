import sys
import os

print("Current Working Directory:", os.getcwd())
print("Python Path:")
for path in sys.path:
    print(path)