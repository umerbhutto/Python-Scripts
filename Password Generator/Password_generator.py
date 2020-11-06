# Password Generator

# Rules for passwords:
#   Easy Password:
#       1. Lower case letters only

#   Medium Password:
#       1. Lower Case letters
#       2. Upper Case Letters
#       3. Numbers

#   Hard Password:
#       1. 5 Lower case letters
#       2. 2 Upper case letters
#       3. 6 Numbers
#       4. 2 Special Characters

# Import the random module
import random as rand

# lower case letters
lower_alphabet = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'
lower_alphabet = lower_alphabet.split()

# Function to choose the lower case letters
def lower_case(user_range = 8):
    global lower_selection
    lower_selection = []
    for i in range(0,user_range):
        guess = rand.randint(0,len(lower_alphabet)-1)
        guess = str(lower_alphabet[guess])
        lower_selection.append(guess)
    lower_selection = ''.join(lower_selection)

# Upper case letters
upper_alphabet = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'
upper_alphabet = upper_alphabet.split()

# Function to choose the upper case letters
def upper_case(user_range = 8):
    global upper_selection
    upper_selection = []
    for i in range(0,user_range):
        guess = rand.randint(0,len(upper_alphabet)-1)
        guess = str(lower_alphabet[guess])
        upper_selection.append(guess)
    upper_selection = ''.join(upper_selection)

# Numeric
numeric = '0 1 2 3 4 5 6 7 8 9'
numeric = numeric.split() 

# Function to choose the numbers
def digits(user_range = 8):
    global num_selection
    num_selection = []
    for i in range(0,user_range):
        guess = rand.randint(0,len(numeric)-1)
        guess = str(numeric[guess])
        num_selection.append(guess)
    num_selection = ''.join(num_selection)
    num_selection = str(num_selection)

# Special Characters
special_charac = '! @ # $ % & * ^ ?'
special_charac = special_charac.split()

# Function to choose the special characters
def special(user_range = 5):
    global spec_selection
    spec_selection = []
    for i in range(0,user_range):
        guess = rand.randint(0,len(special_charac)-1)
        guess = str(special_charac[guess])
        spec_selection.append(guess)
    spec_selection = ''.join(spec_selection)

# Function to shuffle words
def shuffle_pass(orig_pass):
    import random
    word = orig_pass
    shuffled = list(word)
    random.shuffle(shuffled)
    shuffled = ''.join(shuffled)
    global returned_val
    returned_val = shuffled 

# User input to select the type of password
print("This is a password generator")
print("An easy password only has lower case letter\
    \nA medium password has lower case letters upper case letters and numbers\
    \nA hard password has lower case letters, upper case letters, numbers and special characters")
user_choice = input("Do you want an easy / medium / hard password? ")

# Easy password
if user_choice == "easy":
    lower_range = int(input("How many lower case letters do you want? "))
    lower_case(lower_range)
    print("The password is {}.".format(lower_selection))

# Medium password
elif user_choice == "medium":
    # Select number of lower case letters and create the lower case letters of password
    lower_range = int(input("How many lower case letters do you want? "))
    lower_case(lower_range)

    # Select number of upper case letters and create the upper case letters of password
    upper_range = int(input("How many upper case letters do you want? "))
    upper_case(upper_range)

    # Select number of numeric digits and create teh numeric phrase of password
    num_range = int(input("How many numeric digits do you want? "))
    digits(num_range)

    # Merge the various lists and randomly shuffle all of the letters
    my_password = lower_selection + upper_selection + num_selection
    shuffle_pass(my_password)
    print("The password is {}".format(returned_val))

# Hard password
elif user_choice == "hard":
    # Select number of lower case letters and create the lower case letters of password
    lower_range = int(input("How many lower case letters do you want? "))
    lower_case(lower_range)

    # Select number of upper case letters and create the upper case letters of password
    upper_range = int(input("How many upper case letters do you want? "))
    upper_case(upper_range)

    # Select number of numeric digits and create the numeric phrase of password
    num_range = int(input("How many numeric digits do you want? "))
    digits(num_range)

    # Select number of special characters and create the special phrase of password
    spec_range = int(input("How many special characters do you want? "))
    special(spec_range)

    # Merge the various lists and randomly shuffle all of the letters
    my_password = lower_selection + upper_selection + num_selection + spec_selection
    shuffle_pass(my_password)
    print("The password is {}".format(returned_val))