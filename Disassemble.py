import sys
import os

opcodeStr = []
instrSpaced = []
arg1 = []
arg2 = []
arg3 = []
argStr1 = []
argStr2 = []
argStr3 = []
binMem = []
opcode = []
mem = []
instructions = []


specialMask = 0x1FFFF
rnMask = 0x3E0
rmMask = 0x1F0000
rdMask = 0x1F
imMask = 0x3FFC00
shmtMask = 0xFC00
addrMask = 0x1FF000
addr2Mask = 0xFFFFE0
imsftMask = 0x600000
imdataMask = 0x1FFFE0
opcodeStr = []

class TestMe:

    #def __init__(self):

    def run(self):
        global opcodeStr
        global arg1
        global arg2
        global arg3
        global argStr1
        global argStr2
        global argStr3
        global mem
        global binMem
        global opcode

        mem = []
        binMem = []




    def bin2StringSpaced(s):
        spacedStr = s[0:11] + " " + s[12:16] + " " + s[17:22] + " " + s[23:27] + " " + s[28:32]
        return spacedStr
    # def converter(num, bitsize):


    def bin2StringSpacedD(s):
        spacedStr = s[0:11] + " " + s[11:20] + " " + s[20:22] + " " + s[22:27] + " " + s[27:32]
        return spacedStr


    def doshit(self): #unsure how to get this to work..
        with open("test.txt", "r") as f:
            for i in f:
                if opcode[i] == 1112:
                    opcodeStr.append("ADD")
                    arg1.append((int(instructions[i], base=2) & rnMask) >> 5)
                    arg2.append((int(instructions[i], base=2) & rmMask) >> 16)
                    arg3.append((int(instructions[i], base=2) & rdMask) >> 0)
                    argStr1.append("\tR" + str(arg3[i]))
                    argStr2.append("\tR" + str(arg1[i]))
                    argStr3.append("\tR" + str(arg2[i]))



    mem = []
    binMem = []
    if __name__ == '__main__':

        for i in range(len(sys.argv)):
            if(sys.argv[i]=='-i' and i < (len(sys.argv)-1)):
                inputFile = sys.argv[i+i]
                print inputFile
            elif(sys.argv[i] == '-o' and i < (len(sys.argv)-1)):
                outputFile = sys.argv[i+1]

        with open("test.txt", "r") as f:
            for line in f:
                line = bin2StringSpaced(line) #converting the line to string
                instructions = line = #setting instructions to line
                print instructions[0:11] #Just printing to make sure im right
                print (int(line[0:11], base=2)) #prints the decimal version of the opcode.






