message = input("ENTER MESSAGE: ")
cipher = int(input("KEY: "))

def caesar(message, cipher): 
  cipherText = ""
  for ch in message:
    if ch.isalpha():
      stayInAlphabet = ord(ch) + cipher
      if stayInAlphabet > ord('z'):
        stayInAlphabet -= 26
      finalLetter = chr(stayInAlphabet)
      cipherText += finalLetter
  print(cipherText)
  return cipherText

caesar(message, cipher)
