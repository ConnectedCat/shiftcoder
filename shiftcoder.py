import argparse
from string import ascii_lowercase as alphabet
from collections import deque

parser = argparse.ArgumentParser(description='Shift decode')
parser.add_argument('cypherstring', help='string to decode')
args = parser.parse_args()

alphaDeque = deque(alphabet)
for shiftNum in range(26):
    rotatedAlphaDeque = deque(alphabet)
    rotatedAlphaDeque.rotate(-shiftNum)
    newString = ''
    for char in list(args.cypherstring):
        key = list(rotatedAlphaDeque).index(char)
        newString += alphaDeque[key]
    print 'Shift by '+ str(shiftNum)+': '+newString
