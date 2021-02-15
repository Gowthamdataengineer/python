from time import sleep


import sys

string = """  some random content here """
for letter in string:
  sleep(0.01) # In seconds
  sys.stdout.write(letter)
  sys.stdout.flush()
