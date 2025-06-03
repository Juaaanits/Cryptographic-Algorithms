'''A program that encrypts and decrypts message through columnar-transposition-cipher cryptographic algorithm
Requirements:
    1. message
    2. keyword (e.g. "HACK")
'''


from math import ceil

keyword = "HACK"
#column_count = len(keyword)
keyword_letters = list(keyword)


print(keyword_letters)


sorted_letters = sorted(keyword_letters)
print(sorted_letters)


# Create a function that encrypts the message
def encryptMessage(msg):
    cipher = ""


    return cipher

# Create grid/matrix 
def createGrid(msg, keyword):
    row_count = ceil(len(msg) / len(keyword))
    column_count = len(keyword) 
    return row_count, column_count


# Create a function that decrypts a message
def decryptMessage():
    return


if "__main__":
# Create a driver code for input and output
    msg = "My name is Juanito"
    message, key = createGrid()
'''
    cipher = encryptMessage(msg)
    print("Encrypted Message: {}".format(cipher))
    print(decryptMessage(cipher))
'''

