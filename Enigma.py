#!/usr/bin/env python
#
# Encryption & Decryption
#
from argparse import ArgumentParser 
from string import ascii_lowercase as alphabets

class Enigma(object):
  __version__ = 1.0
  def __init__(self,text=None,file=None):
   self.text = text if text else None
   self.file = file if file else None

  def write(self,file,text):
    with open(file,'a') as write_to_file:
     write_to_file.write('{} '.format(text))
  
  def fward(self,letter):
     x=alpha.index(letter.lower())
     for i in range(key):
      x = x+1 if x != 25 else 0
      letter = alpha[x]
     return letter

  def bward(self,letter):
    x=alpha.index(letter.lower())
    for i in range(key):
     x = x-1 if x != 0 else 25
     letter = alpha[x] 
    return letter

  def encrypt(self,text):
    _msg=[]  
    for item in text:
     _msg.append(self.bward(item)if n else self.fward(item))
     self.flip()
    return ''.join(_msg)

  def decrypt(self,text):
    _msg = []
    for item in text:
     _msg.append(self.fward(item)if n else self.bward(item))
     self.flip()
    return ''.join(_msg)

  def process(self):
    if _encrypt:
     if output:
      self.write(output,self.encrypt(self.text))
     else:
      print ('\n{}\n'.format(self.encrypt(self.text)))

    if _decrypt:
     if output:
      self.write(output,self.decrypt(self.text))
     else:
      print ('\n{}\n'.format(self.decrypt(self.text)))

  def read(self):
    with open(self.file,'r') as reader:
     for line in reader:
      text = []
      for item in line:
       if item == ' ': 
        text.append(' ');continue
       if item == '\n':
        text.append('\n');continue
       if not str(item).lower() in alpha:
        continue
       if _encrypt:
        text.append(self.encrypt(item))
       if _decrypt:
        text.append(self.decrypt(item))
      if output:
       self.write(output,'{} '.format(''.join(text)))
      else:
       print ('{}'.format('{}'.format(''.join(text))))

  def flip(self):
    global n
    n=0 if n else 1
    return n
 
if __name__ == '__main__':
  alpha = list(alphabets)
  
  # Assign Arugments
  User = ArgumentParser()
  User.add_argument('key',help='lock & unlock pin')
  User.add_argument('-f', help='file to read from ',dest='file')
  User.add_argument('-o', help='file to write to',dest='output')
  User.add_argument('-m', help='message to process',dest='msg')
  User.add_argument('--lock', help='encrypt data',dest='lock',action='store_true')
  User.add_argument('--unlock', help='decrypt data',dest='unlock',action='store_true')
  args = User.parse_args()
 
  # Assign Variables
  msg      = args.msg
  output   = args.output
  _file    = args.file
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

  n   = 0
  key = eval(args.key)
  run = Enigma(msg,_file)
 
  # Engine Start
  if msg:
   run.process()
   
  if _file:
   run.read()    
