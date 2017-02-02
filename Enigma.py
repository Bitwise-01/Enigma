#!/usr/bin/env python
#
# Encryption & Decryption
#
from string import ascii_lowercase as alphabets

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

def encrypt():
  _msg = [fward(item)if not k%2 else bward(item)for k,item in enumerate(msg)]
  return ''.join(_msg)   

def decrypt():
  _msg = [bward(item)if not k%2 else fward(item)for k,item in enumerate(msg)]
  return ''.join(_msg)
   
if __name__ == '__main__':
  alpha = list(alphabets)
  try:
   msg = raw_input('[-] Enter your msg: ')
   key = int(input('[+] Enter your key: '))
   EnD = int(input('\n0: Encrypt\n1: Decrypt\n[+] Enter option: '))
   print ('\n\nOutput: {}\n'.format(decrypt() if EnD else encrypt()))
  except KeyboardInterrupt:exit('')
