"""
Names: Dalton Melville, Diego Santana
NetIDs: Drm143, dsp50
"""
import sys
import os

""" Lists """
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
opcodeStr = []
mem = []
instructions = []
Memory = 96

""" Masks """
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



class TestMe:

    # def __init__(self):
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
        global inputFile
        global instructions
        global instrSpaced
        global Memory

        for i in range(len(sys.argv)):
            if (sys.argv[i] == '-i' and i < (len(sys.argv) - 1)):
                inputFile = sys.argv[i + i]
            elif (sys.argv[i] == '-o' and i < (len(sys.argv) - 1)):
                outputFile = sys.argv[i + 1]

        #Gets the Instrutcions from the input file.
        def get_instructions(inputFile):
            with open(inputFile, "r") as f:
                for line in f:
                    instructions.append(line)

        #Converting the Binary to a spaced string (From Greg) "R" for Instruction Formatting.
        def bin2StringSpaced_R(s):
            spacedStr = s[0:11] + " " + s[11:16] + " " + s[16:22] + " " + s[22:27] + " " + s[27:32]
            return spacedStr

        get_instructions(inputFile)
        outputFile = open(outputFile + "_dis.txt", 'w')

        for i in range(len(instructions)):
            instrSpaced.append(bin2StringSpaced_R(instructions[i]))
            opcode.append(int(instructions[i][0:11], base=2))
            if int(opcode[i]) == 1112:
                opcodeStr.append(" ADD")
                arg1.append((int(instructions[i], base=2) & rnMask) >> 5)
                arg2.append((int(instructions[i], base=2) & rmMask) >> 16)
                arg3.append((int(instructions[i], base=2) & rdMask) >> 0)
                argStr1.append("\tR" + str(arg3[i]))
                argStr2.append("\tR" + str(arg1[i]))
                argStr3.append("\tR" + str(arg2[i]))
            elif int(opcode[i]) == 1624:
                opcodeStr.append("SUB")
                arg1.append((int(instructions[i], base=2) & rnMask) >> 5)
                arg2.append((int(instructions[i], base=2) & rmMask) >> 16)
                arg3.append((int(instructions[i], base=2) & rdMask) >> 0)
                argStr1.append("\tR" + str(arg3[i]))
                argStr2.append("\tR" + str(arg1[i]))
                argStr3.append("\tR" + str(arg2[i]))
            else: #Anything that is not ADD or SUB
                opcodeStr.append("")
                arg1.append((int(instructions[i], base=2) & rnMask) >> 5)
                arg2.append((int(instructions[i], base=2) & rmMask) >> 16)
                arg3.append((int(instructions[i], base=2) & rdMask) >> 0)
                argStr1.append("\tR" + str(arg3[i]))
                argStr2.append("\tR" + str(arg1[i]))
                argStr3.append("\tR" + str(arg2[i]))

            #Write the formatting to the File.
            outputFile.write(instrSpaced[i] + "    " + str(Memory) + "   " + opcodeStr[i] + argStr1[i] + ", " +
                             argStr2[i] + ", " + argStr3[i] + "\n")
            Memory += 4

        return


if __name__ == '__main__':
    test = TestMe()
    test.run()






