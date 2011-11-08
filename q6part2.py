#automata homework 1 part 2 - fall 2011 bilkent university
#author: onur senture http://github.com/onursenture
# -*- coding: utf-8 -*-

#TODO: turkish chars cannot be handled

import re

ext = "pdf"
idConsist = 8

def verify(line):

    #verification 1: starts with 19, 20, or 21
    p = re.compile('^(19|20|21)')
    if p.search(line) == None:
        return False
        
    #verification 2: id consists of 8 digits
    l = re.compile(r'-*_*\s*\.*').split(line)
    if len(l[0]) != idConsist:
        return False

    #verification 3: wrong extension
    if l.pop() != ext:
        return False

    return True

def write(line, wrongOrWhat):
    if wrongOrWhat == False:
        print line, "\tWRONG FORMAT!"
    else:
        out = ""
        l = re.compile(r'-*_*\s*\.*').split(line)

        counter = 0
        behaveNormal = False

        #assuming that there can be only one middle name
        if len(l) == 4: #standard input
                    behaveNormal = True
        
        for eh in l:
            if eh != l[-1]:
                out += eh
                if counter != 1:
                    out += "\t"
                else:
                    out += " "
                
                if not behaveNormal:
                    counter = counter + 1

        print out

def controller():

    allLines = [line.strip() for line in open("homeworks.txt")]
    for line in allLines:
        if verify(line):
            write(line, True)
        else:
            write(line, False)

if __name__ == "__main__":
    controller()
