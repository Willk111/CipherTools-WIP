def generate_key_square(keyword):
    # Remove duplicates from keyword and merge with the alphabet (excluding 'J')
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # 'I' and 'J' are treated as the same
    key_square = []
    used_chars = set()

    for char in keyword.upper():
        if char not in used_chars and char != 'J':
            key_square.append(char)
            used_chars.add(char)

    for char in alphabet:
        if char not in used_chars:
            key_square.append(char)

    # Return the key square as a 5x5 grid
    return [key_square[i * 5:(i + 1) * 5] for i in range(5)]

# Helper function to find the position of a letter in the key square
def find_position(letter, key_square):
    for row in range(5):
        for col in range(5):
            if key_square[row][col] == letter:
                return row, col
    return None

# Decrypt a pair of letters using the Playfair cipher rules
def decrypt_pair(pair, key_square):
    row1, col1 = find_position(pair[0], key_square)
    row2, col2 = find_position(pair[1], key_square)

    # Same row: move left
    if row1 == row2:
        return key_square[row1][(col1 - 1) % 5] + key_square[row2][(col2 - 1) % 5]
    # Same column: move up
    elif col1 == col2:
        return key_square[(row1 - 1) % 5][col1] + key_square[(row2 - 1) % 5][col2]
    # Rectangle: swap columns
    else:
        return key_square[row1][col2] + key_square[row2][col1]

# Format the ciphertext into pairs of letters
def prepare_ciphertext(ciphertext):
    ciphertext = ciphertext.upper().replace('J', 'I')
    digraphs = []

    i = 0
    while i < len(ciphertext):
        a = ciphertext[i]
        b = ciphertext[i + 1] if i + 1 < len(ciphertext) else 'X'

        if a == b:
            digraphs.append(a + 'X')  # If both letters are the same, insert 'X'
            i += 1
        else:
            digraphs.append(a + b)
            i += 2

    return digraphs

# Main decryption function
def playfair_decrypt(ciphertext, keyword):
    key_square = generate_key_square(keyword)
    digraphs = prepare_ciphertext(ciphertext)
    plaintext = ''

    for digraph in digraphs:
        plaintext += decrypt_pair(digraph, key_square)

    return plaintext