import argparse
# let's bring all of the latin alphabet characters in lower case
from string import ascii_lowercase as alphabet
# deque alows for easy shifting of a list of items
from collections import deque

# this allows us to take arguments from the terminal command
# we'll pass whatever we need to decode and store it in args.cypherstring
parser = argparse.ArgumentParser(description='Shift decode')
parser.add_argument('cypherstring', help='string to decode')
args = parser.parse_args()

# turn the alphabet into a list of letters
alphaDeque = list(alphabet)
# loop through all the shift possibilities, so 26 times
for shiftNum in range(26):
    # make a deque from the alphabet for easy shifting
    # and shift it left (so -) by the shift number
    rotatedAlphaDeque = deque(alphabet)
    rotatedAlphaDeque.rotate(-shiftNum)
    # make an empty container for the new option
    newString = ''
    # loop through every letter in our cypherstring
    # we need to convert the cypherstring into a list and
    # make sure all the characters are lowercase to avoid errors
    for char in list(args.cypherstring.lower()):
        # get the position of a letter in the rotated alphabet
        key = list(rotatedAlphaDeque).index(char)
        # grab the letter at that position in the original alphabet
        # and add it to the container for the new option
        newString += alphaDeque[key]
    # print the resulting option for each of the 26 shifts
    print 'Shift by '+ str(shiftNum)+': '+newString
