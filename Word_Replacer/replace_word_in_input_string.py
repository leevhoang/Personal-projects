# Lee Hoang
# 24 May 2017
# Python Project
#
# This program will take a string as input and replace every instance of that word
# with that of the user's choice.
# The code I wrote is based off of an implementation on gomputer.wordpress.com.
# .items() is used since iteritems() is considered deprecated.
#
# CHANGELOG:
#
# 24 May 2017 - Set up project. It can currently modify hardcoded words in a
# sentence inputted by the user.
#
# 30 May 2017 - Revamped the program to handled external files. Now it prompts the user
# for the words to replace and the replacements. Currently, this program modifies a copy
# of the original text in the file before printing the result to the screen.
#
# 2 June 2017 - Modified the code to output the altered text to a new text file.
#
# 20 June 2017 - NEXT PLAN: Allow multiple words to be replaced in one session.
#
# 17 October 2017 - Removed old code. This version was submitted to GitHub.
#
# 23 October 2017 - Submitted to GitHub.
#


# Open a file to modify.
try:
    filename = input("Enter the name of the text file that you want to modify:\n")
    file = open(filename, "r") # Open the file in read-only mode.
    text = file.read() # Begin reading the file.
except: # No file is found.
    print("Sorry, we could not find the specified filename.")
else: # File is successfully opened.
    print("File", filename, "opened.")

    # Enter the word to replace along with its replacement.
    to_replace = input("Enter the word you want to replace:\n")
    replacement = input("Now enter the new word:\n")

    # Get the name of the new textfile from the user.
    alt_filename = input("Please enter the name of the new textfile to write to:\n")
    alt_file = open(alt_filename, "w+") # Open the new text file in write + mode.

    # Create a dictionary object containing the above.
    rep = {to_replace:replacement}

    # Replace all of the selected words in the text file.
    for i, j in rep.items():
        file_read = text.replace(i, j)

    alt_file.write(file_read) # Write the resulting text to the new textfile.

    # Print the contents of the file before closing it.
    print("\nThis is the result of the word changes:\n-----------------------------\n")
    print(file_read)
    file.close() # Close the file afterwards.
    alt_file.close() # Close the new file.
