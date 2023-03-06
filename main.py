########################################
#              COP3502C                #
#               Lab 6                  #
#           Encoder/Decoder            #
#       Blake Owen, Braden Azis        #
########################################

# encode function that adds 3 to each digit
def encode(password):
    encode_p = ''
    for i in range(len(password)):  # loops through each digit of password passed through
        digit = int(password[i]) + 3  # adds 3 to each looped digit

        if digit > 9:  # checks if digit becomes greater than 9, and subtracts 10 if true
            digit -= 10

        digit = str(digit)  # converts digit to string and adds it to existing string variable encode_p
        encode_p += digit

    return encode_p


# Decode function that takes the encoded password and subtracts 3 from each digit returning the original password
# Written by Blake Owen
def decode(encoded):
    original = ''

    for i in range(len(encoded)):   # loops through each digit subtracting 3 from each
        digit = int(encoded[i]) - 3
        if digit < 0:      # checks if digit is less than 0, wraps around to 9
            digit += 10
            original += str(digit)
        else:
            original += str(digit)

    return original


# main function of the program with menu
def main():
    program_run = True
    while program_run:
        print('''Menu  
------------- 
1. Encode  
2. Decode  
3. Quit\n''')

        option = int(input('Please enter an option: '))

        if option == 1:
            password = (input('Please enter your password to encode: '))

            encoded_pass = encode(password)

            print('Your password has been encoded and stored!\n')

        elif option == 2:
            try:    # Exception handling in case no password has been encoded
                print("The encoded password is " + encoded_pass + ", and the original password is "
                      + decode(encoded_pass) + ".\n")   # Encoded and original passwords are printed to user

            except UnboundLocalError:   # UnboundLocalError is raised if no password was encoded
                print("Error! No password was encoded!\n")

        elif option == 3:
            program_run = False

        else:
            print('Error! Invalid selection!')


if __name__ == '__main__':
    main()
