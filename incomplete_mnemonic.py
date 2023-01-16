'''
This code imports the Mnemonic class from the mnemonic module and
creates an instance of the class using the "english" language.
It then sets a variable "words" to the list of all possible words in
a BIP39 mnemonic, and a variable "mnemonic" to an incomplete mnemonic
string. It splits the mnemonic into a list of words, and calculates the total 
number of combinations of missing 8th and 9th words by multiplying the 
length of the word list. The code then initializes a counter variable, and uses
nested for loops to iterate through all possible combinations of the 8th and 9th
words in the mnemonic. For each combination, it generates a new mnemonic by updating
the mnemonic_words list and joining the words together. It then checks if the new
mnemonic is valid using the check() method of the Mnemonic class, and if so, it
prints the valid mnemonic. It then updates the counter variable, calculates the
progress, and prints it to the console. Finally, it sleeps for 0.1 seconds before
moving on to the next iteration. The purpose of this code is to check all possible 
combinations of the 8th and 9th words in the incomplete mnemonic and find any valid mnemonics.
'''
import time
from mnemonic import Mnemonic
mnemo = Mnemonic("english")

# List of all possible words in a BIP39 mnemonic
words = mnemo.wordlist

# The incomplete mnemonic
mnemonic = "intact pass airport pink embrace later caught ancient pave"

# Split the mnemonic into a list of words
mnemonic_words = mnemonic.split()

# Get the total number of combinations
total_combinations = len(words) * len(words)

# Initialize a counter for the number of checked combinations
counter = 0

# Check all possible combinations of the missing eighth and ninth words
for i in range(len(words)):
    for j in range(len(words)):
        # Generate a new mnemonic with the current combination of words
        mnemonic_words[7] = words[i]
        mnemonic_words[8] = words[j]
        new_mnemonic = " ".join(mnemonic_words)
        if mnemo.check(new_mnemonic):
            print("Valid mnemonic:", new_mnemonic)
        
        # Update the counter and print the progress
        counter += 1
        progress = (counter / total_combinations) * 100
        print("Progress: {:.2f}%".format(progress), end='\r')
        time.sleep(0.1)
