#automata homework 1 part 1 - fall 2011 bilkent university
#author: onur senture http://github.com/onursenture

import re

def readLines():

    doesNotContain_101 = 0
    containsCon1s = 0
    starts11_ends01 = 0
    doesNotMoreThanOne = 0

    allLines = [line.strip() for line in open("inputs.txt")]
    for line in allLines:

        #part a - 1
        p = re.compile('101+')
        if p.search(line) == None:
            doesNotContain_101 = doesNotContain_101 + 1

        #part a - 2
        p = re.compile('11+')
        if p.search(line) != None:
            containsCon1s = containsCon1s + 1

        #part a - 3
        p = re.compile('^11.*01$' )
        if p.search(line) != None:
            starts11_ends01 = starts11_ends01 + 1

        #part a -4
        p = re.compile('(00)?') #TODO: does not work properly right now
        if p.search(line) == None:
            print p.search(line)
            doesNotMoreThanOne = doesNotMoreThanOne + 1

    print "# of strings that does not contain 101: ", doesNotContain_101
    print "# of strings that contains at least one pair of consecutive 1s: ", containsCon1s
    print "# of strings that starts with 11 and ends with 01: ", starts11_ends01
    print "# of strings that does not contain more than one occurence of the string 00: ", doesNotMoreThanOne

if __name__ == "__main__":
    readLines()