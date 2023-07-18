import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
print(art.logo)

def caesar(txt, shift_count, direct):
    def encrypt(plain_text, shift_amount):
        cipher_text = ""
        length_of_alphabet = len(alphabet)
        for i in plain_text:
            if i in alphabet:
                index_of_letter = alphabet.index(i)
                shifted_index = index_of_letter + shift_amount
                if shifted_index >= len(alphabet):
                    new_index = shifted_index - length_of_alphabet
                    cipher_text += alphabet[new_index]
                else:
                    cipher_text += alphabet[shifted_index]
            else:
                cipher_text += i

        print(f"The encrypted text is {cipher_text}")


    def decrypt(cipher_text, shift_amount):
        plain_text = ""
        for i in cipher_text:
            if i in alphabet:
                index_of_letter = alphabet.index(i)
                back_shifted = index_of_letter - shift_amount
                plain_text += alphabet[back_shifted]
            else:
                plain_text += i
        print(f"The decrypted text is {plain_text}")

    if direct == "encode":
        encrypt(plain_text=txt, shift_amount=shift_count)

    else:
        decrypt(cipher_text=txt, shift_amount=shift_count)


again = False
while not again:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if direction == "encode" or direction == "decode":
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        if shift > 26:
            shift = shift % 26
        caesar(txt=text, shift_count=shift, direct=direction)
        answer = input("Do you want to restart the cipher program? (yes/no)").lower()
        if answer == "no":
            again = True
            print("The cipher program has end.")

    else:
        print("Wrong")

# TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar().             DONE
# TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.              DONE

# eğer encodingde shift yaparken liste sonuna gelirse tekrar liste başına dönmesini sağla                   DONE
#TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?        DONE
#Try running the program and entering a shift number of 45.
#Add some code so that the program continues to work even if the user enters a shift number greater than 26.
#Hint: Think about how you can use the modulus (%).
#TODO-1: Import and print the logo from art.py when the program starts.                                     DONE

#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?               DONE
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a while loop that continues to execute the program if the user types 'yes'.
#TODO-3: What happens if the user enters a number/symbol/space?                                             DONE
    #Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
    #e.g. start_text = "meet me at 3"
    #end_text = "•••• •• •• 3"

#TODO: lowercase/uppercase e dikkat et
#TODO: girdi farklı olduğunda wrong mesajını verip tekrar girdi istemeli