alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#Don't change the code above 👆
  
#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
n_list = list(text)
def encrypt():
  chiper_text = ""
  position = 0
  for i in n_list :
    position = alphabet.index(i)
    new_position = position + shift
    new_letter = alphabet[new_position]
    chiper_text += new_letter
  print(f'The encode message is {chiper_text}')
