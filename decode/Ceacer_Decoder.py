#Ceacer Cyper Decoder By WIlliam K

#User imput for the encoded message
ciphertext = input("Please ender your encoded message: ")
shift = int(input("Please enter the posotive shift number you want to use: "))

#Single letter Decoder Function
def decode_letter(letter, shift):
    if letter.isalpha(): 
        start = ord('A') if letter.isupper() else ord('a')
        #Find the position of the letter in the alphabet
        original_pos = ord(letter) - start
        #Applying the reverse shift (%26 is to ensure alphabet wrap around)
        new_pos = (original_pos - shift) % 26 
        return chr(start + new_pos)
    
    else:
        return letter
    
#Entire message decode function
def decode_message(ciphertext, shift):
    decoded_message = ""

    for char in ciphertext:
        decoded_message += decode_letter(char, shift)

    return decoded_message

decoded_message = decode_message(ciphertext, shift)
print("Decoded message: ", decoded_message )
