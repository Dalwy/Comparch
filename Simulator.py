import disassembler2
import sys


class Simulator:

    def __init__(self):
        pass

    def run(self):
        global outputFile

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
                outputFile.write("====================" + "\n" + "cycle" + str(i+1) + "\t" + str(disassembler2.Memory) +
                                 "\t" + "ADDI" + "\n")
            elif disassembler2.opcodeStr[i] == "B":
                outputFile.write("====================" + "\n" + "cycle" + str(i + 1) + "\t"
                                 + "B" + "\n")
            elif disassembler2.opcodeStr[i] == "ADD ":
                outputFile.write("====================" + "\n" + "cycle" + str(i + 1) + "\t" + "\n")
            elif disassembler2.opcodeStr[i] == "SUB ":
                outputFile.write("====================" + "\n" + "cycle" + str(i + 1) + "\t" + "\n")
            elif disassembler2.opcodeStr[i] == "SUBI":
                outputFile.write("====================" + "\n" + "cycle" + str(i + 1) + "\t" + "\n")
            elif disassembler2.opcodeStr[i] == "AND ":
                outputFile.write("====================" + "\n" + "cycle" + str(i + 1) + "\t" + "\n")
            elif disassembler2.opcodeStr[i] == "ORR ":
                outputFile.write("====================" + "\n" + "cycle" + str(i + 1) + "\t" + "\n")
            elif disassembler2.opcodeStr[i] == "EOR ":
                outputFile.write("====================" + "\n" + "cycle" + str(i + 1) + "\t" + "\n")
            elif disassembler2.opcodeStr[i] == "MOVZ":
                outputFile.write("====================" + "\n" + "cycle" + str(i + 1) + "\t" + "\n")
            print disassembler2.opcodeStr[i]
            i += 1
if __name__ == '__main__':
    test = Simulator()
    test.run()