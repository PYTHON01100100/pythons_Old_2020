"""
import time
word="server is listening............"
for letter in word:
       print(letter, end = "",flush=True)
       time.sleep(1)
"""
import time
word="server is listening............\n"
for letter in range(10):
       for letter in word:
              print(letter, end = "", flush = True)
              time.sleep(1)
