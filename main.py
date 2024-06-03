import string

alphabets = string.ascii_lowercase * 2
encode_inputs = ["encode", "encrypt"]
decode_inputs = ["decode", "decrypt"]
valid_inputs = encode_inputs + decode_inputs


def caesar(cipher_direction, start_text, shift_amount):
    end_text = ""
    dir = "encrypting"
    # if the direction is valid, then make the shift amount negative
    if cipher_direction in decode_inputs:
        dir = "decrypting"
        shift_amount *= -1
    for char in start_text:
        if char in alphabets:
            # get the index
            index = alphabets.index(char)
            # shift the index
            new_index = index + shift_amount
            # add the alphabet at the given index to the end string
            end_text += alphabets[new_index]
        else:
            # if the char is not an alphabet, then add it as it is without shifting
            end_text += char
    print(f"\nText after {dir} is: {end_text}\n")


should_continue = True
while should_continue:
    direction = input("Enter {0} to encrypt or {1} to decrypt: "
                      .format(" or ".join(encode_inputs).casefold(), 
                              " or ".join(decode_inputs))).casefold()
    if direction not in valid_inputs:
        print(f"{direction} is not a valid input.")
        continue
    text = input(f"\nEnter text to {direction}: ").casefold()
    shift = int(input("Enter the shift number: ")) % 26
    caesar(direction, text, shift)

    if input("Do you want to go again? (y/n): ").casefold() != "y":
        should_continue = False
        print("\nExiting.")
    
