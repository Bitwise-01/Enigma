#!/usr/bin/env python
#
# Encryption & Decryption
#
from string import ascii_lowercase as alphabets

def Forward(letter):
  x=alpha.index(letter.lower())
  for i in range(key):
   x = x+1 if x != 25 else 0
   new = alpha[x]
  return new

def Backward(letter):
  x=alpha.index(letter.lower())
  for i in range(key):
   x = x-1 if x != 0 else 25
   new = alpha[x]
  return new

def Encrypt():
  encrypt = [Forward(item) if not k%2 else Backward(item) for k,item in enumerate(msg)]
  return ''.join(encrypt)   

def Decrypt():
  decrypt = [Forward(item) if k%2 else Backward(item) for k,item in enumerate(msg)]
  return ''.join(decrypt)
   
if __name__ == '__main__':
  alpha = list(alphabets)
  try:
   msg = raw_input('[-] Enter your msg: ')
   key = int(input('[+] Enter your key: '))
   EnD = int(input('\n0: Encrypt\n1: Decrypt\n[+] Enter option: '))
   print ('\n\nOutput: {}\n'.format(Decrypt() if EnD else Encrypt()))
  except KeyboardInterrupt:exit('')
