#Vigenère Cipher DEcoder by WIlliam K

#Get the cipher text and key form the user:
ciphertext = input("Please enter the message you would like to decode: ")
keyword = input("Now please enter your keyword: ")

#Processing keyword
def generate_key(cipertext, keyword):
    keyword_repeated = ''
    keyword_length = len(keyword)
    for i in range(len(ciphertext)):
        if ciphertext[i].isalpha():
            keyword_repeted += keyword[i % keyword_length]
        else:
            keyword_repeted += ' '
    return keyword_repeated 

def decode_letter(cipher_letter, key_letter):
    if cipher_letter.isaplha(): #Checks if it actualy is a letter
        start =  ord('A') if cipher_letter.isupper() else ord('a')
        
        cipher_pos = ord(cipher_letter) - start
        key_pos = ord(key_letter.upper()) - ord('A')
        
        decoded_pos = (cipher_pos - key_pos) % 26

