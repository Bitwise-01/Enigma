# Enigma
Encryption Software

# Key
It's used for decrypting. Save the key or memorize it, because without it you can't decrypt the message

# Rules
1) you can either read from a file (-f filname) or process a text (-m text), but not but at once.

2) the program will only run if it has something to encrypt or decrypt (--lock or --unlock), if you don't add those your file or text will not get processed

3) -m only reads one text at a time, so you can't do (-m "Hello World"), but can do (-m helloworld)

4) you must have a key for lock and unlock

5) you can encrypt a whole TEXT file either to display or to a file

6) this program is only for TEXT

# Usage: Enigma.py [-h] [-f FILE] [-o OUTPUT] [-m MSG] [--lock] [--unlock] key

# Demo
# Encrypting:
 Input: python Enigma.py -m helloworld --lock 15
 Output: wpawdhdcao

# Decrypting:
 Input: python Enigma.py -m wpawdhdcao --unlock 15
 Output: helloworld
 
# Encrypt & Save:
 Input: python Enigma.py -o filename -m helloworld --lock 62
  
# Decrypt & Save:
 Input: python Enigma.py -o save_to_file -m ruvbymyhvt --unlock 62

  
