'''Here we can convert text into Morse'''

from converter import Converter

user_input = input("What do you want to convert in Morse code? ")
converter = Converter()
print(f'Your text in Morse code is: {converter.text_to_morse(user_input)}')