#!/usr/bin/env python
#
# Encryption & Decryption
#
from argparse import ArgumentParser 
from string import ascii_lowercase as alphabets

class Enigma(object):  
  def __init__(self,text=None,_file=None):
   self.file = _file
   self.text = text 
   self.key  = key
   self.flip = 0

  def write(self,file,text):
    with open(file,'a') as write_to_file:
     write_to_file.write('{} '.format(text))
  
  def fward(self,letter):
     x=alpha.index(letter.lower())
     for i in range(self.key):
      x = x+1 if x != 25 else 0
      letter = alpha[x]
     return letter

  def bward(self,letter):
    x=alpha.index(letter.lower())
    for i in range(self.key):
     x = x-1 if x != 0 else 25
     letter = alpha[x] 
    return letter
 
  def mod(self):
   return (self.key*17+inc+abs(self.key/inc))%104729
    
  def encrypt(self,text):
    _msg=[]  
    for item in text:
     self.key  = self.mod()
     _msg.append(self.bward(item)if self.flip else self.fward(item))
     self.flip = 0 if self.flip else 1
    return ''.join(_msg).lower()

  def decrypt(self,text):
    _msg = []
    for item in text:
     self.key  = self.mod()
     _msg.append(self.fward(item)if self.flip else self.bward(item))
     self.flip = 0 if self.flip else 1
    return ''.join(_msg).lower()

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

if __name__ == '__main__':
  alpha = list(alphabets)
  
  # assign arugments
  user = ArgumentParser()
  user.add_argument('key',help='lock & unlock pin')
  user.add_argument('inc',help='incremental key')
  user.add_argument('-f', help='file to read from ',dest='file')
  user.add_argument('-o', help='file to write to',dest='output')
  user.add_argument('-m', help='message to process',dest='msg')
  user.add_argument('--lock', help='encrypt data',dest='lock',action='store_true')
  user.add_argument('--unlock', help='decrypt data',dest='unlock',action='store_true')
  args = user.parse_args()
 
  # assign variables
  msg      = args.msg
  output   = args.output
  _file    = args.file
  _encrypt = args.lock
  _decrypt = args.unlock

  # logic
  if _file:
   msg=None

  if msg:
   _file=None

  if _decrypt:
   _encrypt=None

  if _encrypt:
   _decrypt=None

  # few configs
  inc = eval(args.inc)
  key = eval(args.key)
  run = Enigma(msg,_file)
 
  # start process
  if msg:
   run.process()
   
  if _file:
   run.read()    
