FIRST_CHAR_CODE = ord("A")  # Gets the ASCII code for 'A' (65), used as the starting point for uppercase letters.
LAST_CHAR_CODE = ord("Z")   # Gets the ASCII code for 'Z' (90), used as the ending point for uppercase letters.
CHAR_RANGE = LAST_CHAR_CODE - FIRST_CHAR_CODE + 1  # Calculates the total number of uppercase letters (26), for wrapping shifts around the alphabet.

def caesar_criphert(message, shift):  # Defines a function named 'caesar_criphert' (note: likely a typo for 'caesar_cipher') that takes a message string and an integer shift value.

    result = ""  # Initializes an empty string to build the encrypted result.

    for char in message.upper():  # Loops through each character in the message, converting the entire message to uppercase first (so only uppercase letters are shifted; others are unchanged).

        if char.isalpha():  # Checks if the current character is an alphabetic letter (A-Z).

            char_code = ord(char)  # Gets the ASCII code of the current character (e.g., 'A' is 65).

            new_char_code = char_code + shift  # Adds the shift value to the ASCII code to get the new position (e.g., 'A' + 3 = 68, which is 'D').

            if new_char_code > LAST_CHAR_CODE:  # If the new code exceeds 'Z' (90), wraps around to the start of the alphabet.
                new_char_code -= CHAR_RANGE  # Subtracts 26 to wrap (e.g., 'Z' + 1 becomes 'A').

            if new_char_code < FIRST_CHAR_CODE:  # If the new code is below 'A' (65, for negative shifts), wraps around to the end of the alphabet.
                    new_char_code += CHAR_RANGE  # Adds 26 to wrap (e.g., 'A' - 1 becomes 'Z').

            new_char = chr(new_char_code)  # Converts the new ASCII code back to a character (e.g., 68 becomes 'D').

            result += new_char  # Appends the new character to the result string.

        else:  # If the character is not alphabetic (e.g., space, punctuation), leaves it unchanged.
            result += char  # Appends the original character to the result string.

    print(result)  # Prints the final encrypted result string to the console (does not return it, so the function can't be reused easily).

user_message = input("Message to Encrypt: ")  # Prompts the user to enter a message string via console input.

user_shift_key = int(input("Shift Key (Integer): "))  # Prompts the user to enter an integer shift key via console input, converting it to int.

caesar_criphert(user_message, user_shift_key)  # Calls the function with the user's message and shift key, executing the encryption and printing the result.
