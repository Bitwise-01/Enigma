# Enigma
Encryption Software

# Key & Inc
They are used for decrypting. Save them or memorize them, because without them you can't decrypt the message

# Rules
1) you can either read from a file (-f filname) or process a text (-m text), but not both at once.

2) the program will only run if it has something to encrypt or decrypt (--lock or --unlock), if you don't add those your file or text will not get processed

3) -m only reads one text at a time, so you can't do (-m "Hello World"), but can do (-m helloworld)

4) you must have a key for lock and unlock

5) you can encrypt a whole TEXT file either to display or to a file

6) this program is only for TEXT

7) beware of what pin you use, because some pins will not encrypt your message, for example pin: 26

# usage: Enigma.py [-h] [-f FILE] [-o OUTPUT] [-m MSG] [--lock] [--unlock] key inc

# Demos
# Encrypting:
python Enigma.py -m helloworld --lock 17 3
 
# Decrypting:
python Enigma.py -m yymrglwnr --unlock 17 3
 
# Encrypt & Save:
python Enigma.py -o filename -m helloworld --lock 62 19
  
# Decrypt & Save:
python Enigma.py -o save_to_file -m rxtostvmws --unlock 62 19

# Read File, Encrypt & Display:
python Enigma.py -f filename --lock 46 13
  
# Read File, Decrypt & Display:
python Enigma.py -f filename --unlock 46 13
  
# Read File, Encrypt & Save:
python Enigma.py -f filename -o locked_file --lock 58 23
  
# Read File, Decrypt & Save:
python Enigma.py -f filename -o unlocked_file --unlock 56 23
