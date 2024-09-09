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
            keywrd_repeted += keyword[i % keyword_length]
        else:
            keyword_repeted += ' '
    return keyword_repeated 



