import disassembler2
import sys


class Simulator:

    def __init__(self):
        pass

    def run(self):
        global outputFile
        global Memory

        Memory = 96
        for i in range(len(sys.argv)):
            if (sys.argv[i] == '-i' and i < (len(sys.argv) - 1)):
                inputFile = sys.argv[i + i]
            elif (sys.argv[i] == '-o' and i < (len(sys.argv) - 1)):
                outputFile = sys.argv[i + 1]
        outputFile = open(outputFile + "_sim.txt", 'w')
        d = disassembler2.TestMe()
        d.run()
        i = 0
        while disassembler2.opcodeStr[i] != 'BREAK':
            if disassembler2.opcodeStr[i] == "ADDI":
                outputFile.write("====================" + "\n" + "cycle " + str(i+1) + "\t" + str(Memory)
                                 + "\t" + "ADDI" + "\n")
            elif disassembler2.opcodeStr[i] == "B ":
                outputFile.write("====================" + "\n" + "cycle " + str(i + 1) + "\t" + str(Memory)
                                 + "\t" + "B" + "\n")
            elif disassembler2.opcodeStr[i] == "ADD ":
                outputFile.write("====================" + "\n" + "cycle " + str(i + 1) + "\t" + str(Memory)
                                 + "\t" + "ADD" + "\n")
            elif disassembler2.opcodeStr[i] == "SUB ":
                outputFile.write("====================" + "\n" + "cycle " + str(i + 1) + "\t" + str(Memory)
                                 + "\t" + "SUB" + "\n")
            elif disassembler2.opcodeStr[i] == "SUBI":
                outputFile.write("====================" + "\n" + "cycle " + str(i + 1) + "\t" + str(Memory)
                                 + "\t" + "SUBI" + "\n")
            elif disassembler2.opcodeStr[i] == "AND ":
                outputFile.write("====================" + "\n" + "cycle " + str(i + 1) + "\t" + str(Memory)
                                 + "\t" + "AND" + "\n")
            elif disassembler2.opcodeStr[i] == "ORR ":
                outputFile.write("====================" + "\n" + "cycle " + str(i + 1) + "\t" + str(Memory)
                                 + "\t" + "ORR" + "\n")
            elif disassembler2.opcodeStr[i] == "EOR ":
                outputFile.write("====================" + "\n" + "cycle " + str(i + 1) + "\t" + str(Memory)
                                 + "\t" + "EOR" + "\n")
            elif disassembler2.opcodeStr[i] == "MOVZ":
                outputFile.write("====================" + "\n" + "cycle " + str(i + 1) + "\t" + str(Memory)
                                 + "\t" + "MOVZ" + "\n")
            elif disassembler2.opcodeStr[i] == "MOVK":
                outputFile.write("====================" + "\n" + "cycle " + str(i + 1) + "\t" + str(Memory)
                                 + "\t" + "MOVK" + "\n")
            elif disassembler2.opcodeStr[i] == "STUR":
                outputFile.write("====================" + "\n" + "cycle " + str(i + 1) + "\t" + str(Memory)
                                 + "\t" + "STUR" + "\n")
            elif disassembler2.opcodeStr[i] == "LDUR":
                outputFile.write("====================" + "\n" + "cycle " + str(i + 1) + "\t" + str(Memory)
                                 + "\t" + "LDUR" + "\n")
            elif disassembler2.opcodeStr[i] == "CBZ ":
                outputFile.write("====================" + "\n" + "cycle " + str(i + 1) + "\t" + str(Memory)
                                 + "\t" "CBZ" + "\n")
            elif disassembler2.opcodeStr[i] == "CBNZ":
                outputFile.write("====================" + "\n" + "cycle " + str(i + 1) + "\t" + str(Memory)
                                 + "\t" + "CBNZ" + "\n")
            elif disassembler2.opcodeStr[i] == "ASR":
                outputFile.write("====================" + "\n" + "cycle " + str(i + 1) + "\t" + str(Memory)
                                 + "\t" + "ASR" + "\n")
            elif disassembler2.opcodeStr[i] == "LSL ":
                outputFile.write("====================" + "\n" + "cycle " + str(i + 1) + "\t" + str(Memory)
                                 + "\t" + "LSL" + "\n")
            elif disassembler2.opcodeStr[i] == "LSR ":
                outputFile.write("====================" + "\n" + "cycle " + str(i + 1) + "\t" + str(Memory)
                                 + "\t" + "LSR" + "\n")
            elif disassembler2.opcodeStr[i] == "NOP":
                outputFile.write("====================" + "\n" + "cycle " + str(i + 1) + "\t" + str(Memory)
                                 + "\t" + "NOP" + "\n")
            elif disassembler2.opcodeStr[i] == "BREAK":
                outputFile.write("====================" + "\n" + "cycle " + str(i + 1) + "\t" + str(Memory)
                                 + "\t" + "BREAK" + "\n")
            print disassembler2.opcodeStr[i]
            i += 1
            Memory += 4
if __name__ == '__main__':
    test = Simulator()
    test.run()
