#Vigenère Cipher DEcoder by WIlliam K (Not working atm)

#Get the cipher text and key form the user:
ciphertext = input("Please enter the message you would like to decode (remove all spaces and numbers in the message): ")
keyword = input("Now please enter your keyword: ")

#Processing keyword
def generate_key(ciphertext, keyword):
    keyword_repeated = ''
    keyword_length = len(keyword)
    for i in range(len(ciphertext)):
        if ciphertext[i].isalpha():
            keyword_repeated += keyword[i % keyword_length]
        else:
            keyword_repeated += ' '
    return keyword_repeated 

def decode_letter(cipher_letter, key_letter):
    if cipher_letter.isalpha(): #Checks if it actualy is a letter
        start =  ord('A') if cipher_letter.isupper() else ord('a')
        
        cipher_pos = ord(cipher_letter) - start
        key_pos = ord(key_letter.upper()) - ord('A')
        
        decoded_pos = (cipher_pos - key_pos) % 26
        
        return chr(start + decoded_pos)
    else:
        return cipher_letter
    
def decode_message(ciphertext, keyword):
    decoded_message = ""

    key = generate_key(ciphertext, keyword)
    

    for i in range(len(ciphertext)):

        decoded_message += decode_letter(ciphertext[i], key[i])
    
    return decoded_message


decoded_output = decode_message(ciphertext, keyword)
print("Decoded message:", decoded_output)
        

