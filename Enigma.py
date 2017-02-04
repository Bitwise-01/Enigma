#!/usr/bin/env python
#
# Encryption & Decryption
#
from string import ascii_lowercase as alphabets
import argparse

def fward(letter):
  x=alpha.index(letter.lower())
  for i in range(key):
   x = x+1 if x != 25 else 0
   new = alpha[x]
  return new

def bward(letter): 
  x=alpha.index(letter.lower())
  for i in range(key):
   x = x-1 if x != 0 else 25
   new = alpha[x] 
  return new

def flip():
  global n
  n=0 if n else 1
  return n

def encrypt(text): 
 _msg=[]  
 for item in text:
  _msg.append(bward(item)if n else fward(item))
  flip()
 return ''.join(_msg)
  
def decrypt(text):
  _msg = []
  for item in text:
   _msg.append(fward(item)if n else bward(item))
   flip()
  return ''.join(_msg)  

def write(file,text):
  with open(file,'a') as write_to:
   write_to.write('{} '.format(text))

def process_text(text):
  if _encrypt:
   if output:
    write(output,encrypt(text))
   else:
    print ('\n{}\n'.format(encrypt(text)))

  if _decrypt:
   if output:
    write(output,decrypt(text))
   else:
    print ('\n{}\n'.format(decrypt(text)))

def read_file():
  with open(_file,'r') as reader:
   for line in reader:
    text = []
    for item in line:
     if item == ' ': text.append(' ');continue
     if item == '\n':text.append('\n');continue
     if not str(item).lower() in alpha:
      continue
     if _encrypt:
      text.append(encrypt(item))
     if _decrypt:
      text.append(decrypt(item))
    if output:
     write(output,'{} '.format(''.join(text)))
    else:
     print ('{}'.format('{}'.format(''.join(text))))
    
def main():
  if msg:
   process_text(msg)
   
  if _file:
   read_file()
      
if __name__ == '__main__':
  alpha = list(alphabets)
  
  # Assign Arugments
  User = argparse.ArgumentParser()
  User.add_argument('key',help='lock & unlock pin')
  User.add_argument('-f', help='file to read from ',dest='file')
  User.add_argument('-o', help='file to write to',dest='output')
  User.add_argument('-m', help='message to process',dest='msg')
  User.add_argument('--lock', help='encrypt data',dest='lock',action='store_true')
  User.add_argument('--unlock', help='decrypt data',dest='unlock',action='store_true')
  args = User.parse_args()
 
  # Assign Variables
  n = 0
  msg = args.msg
  output = args.output
  _file = args.file
  _encrypt = args.lock
  _decrypt = args.unlock

  # Logic
  if _file:
   msg=None

  if msg:
   _file=None

  if _decrypt:
   _encrypt=None

  if _encrypt:
   _decrypt=None
  key = eval(args.key)
  main()
