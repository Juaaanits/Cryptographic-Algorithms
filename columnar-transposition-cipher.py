from math import ceil

# Get Column order from the key
def getKeyOrder(key: str) -> list[int]:
    index_key_characters = []
    for i, character in enumerate(key):
        index_key_characters.append((character, i))
    index_key_characters.sort()
    sorted_key_characters = [index for character, index in index_key_characters]

    return sorted_key_characters

# Create grid/matrix 
def createGrid(messageLength: int, keyLength: int) -> tuple[int, int]:
    column_count = keyLength
    row_count = ceil(messageLength / column_count)
    return row_count, column_count

# Create a function that encrypts the message
def encryptMessage(message: str, key: str, fill_space_character: str = 'X'):
    
    message = message.replace(" ", "").upper()
    key = key.upper()

    column_count = len(key)
    row_count, _ = createGrid(len(message), column_count)

    total_cells = row_count * column_count
    fill_space_needed = total_cells - len(message)
    filled_space_version = message + (fill_space_character * fill_space_needed)
    print(f"Filled space version: '{filled_space_version}'")

    grid = [['' for _ in range(column_count)] for _ in range(row_count)]
    index = 0
    for r in range(row_count):
        for c in range(column_count):
            grid[r][c] = filled_space_version[index]
            index += 1 
    
    column_read_order = getKeyOrder(key)

    cipher = ""
    for column_index in column_read_order:
        for r in range(row_count):
            cipher += grid[r][column_index]


    return cipher

# Create a function that decrypts a message
def decryptMessage(cipher: str, key: str, fill_space_character: str = 'X'):
    key = key.upper() 
    column_count = len(key)
    row_count, _ = createGrid(len(cipher), column_count)


    column_fill_order = getKeyOrder(key) 

    grid = [['' for _ in range(column_count)] for _ in range(row_count)]

    num_full_rows = len(cipher) // column_count
    chars_in_last_row = len(cipher) % column_count

    column_lengths = {}
    for i, original_col_index in enumerate(column_fill_order):
        if i < chars_in_last_row:
            column_lengths[original_col_index] = num_full_rows + 1
        else:
            column_lengths[original_col_index] = num_full_rows


    cipher_index = 0

    for original_col_index in column_fill_order:
        current_column_len = column_lengths[original_col_index]
        for r in range(current_column_len):
            grid[r][original_col_index] = cipher[cipher_index]
            cipher_index += 1

    decrypted_text = ""
    for r in range(row_count):
        for c in range(column_count):
            decrypted_text += grid[r][c]

    cleaned_text = decrypted_text.rstrip(fill_space_character)

    return cleaned_text


if __name__ == "__main__":

    print("Columnar Transposition Cipher")
    input_message = "My name is Juanito"
    encryption_key = "HACK"
    fill_space_character = 'X'

    print(f"Message to encrypt: '{input_message}'")
    print(f"Encrypted: '{encryption_key}'")

    encrypted_text = encryptMessage(input_message, encryption_key, fill_space_character)
    print(f"Encrypted: '{encrypted_text}'")

    decrypted_text = decryptMessage(encrypted_text, encryption_key, fill_space_character)
    print(f"Decrypted: '{decrypted_text}'")

    normalized_original_message = input_message.replace(" ", "").upper()
    print(f"Verification: {'SUCCESS' if decrypted_text == normalized_original_message else 'FAILURE'}")
