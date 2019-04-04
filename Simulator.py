import team11project2
import sys


class Simulator:

    def __init__(self):
        pass

    def run(self):
        global outputFile
        global mem_loc

        mem_loc = 96
        for i in range(len(sys.argv)):
            if (sys.argv[i] == '-i' and i < (len(sys.argv) - 1)):
                inputFile = sys.argv[i + i]
            elif (sys.argv[i] == '-o' and i < (len(sys.argv) - 1)):
                outputFile = sys.argv[i + 1]
        outputFile = open(outputFile + "_sim.txt", 'w')
        d = team11project2.Disassemble()
        d.run()
        i = 0
        while team11project2.opcodeStr[i] != 'BREAK':
            if team11project2.opcodeStr[i] == "ADDI":
                outputFile.write("====================" + "\n" + "cycle:" + str(i + 1) + " \t " + str(mem_loc)
                                 + " \t" + "ADDI" + " "+ str(team11project2.argStr1[i]) + ", " +
                                 str(team11project2.argStr2[i]) + ", " + str(team11project2.argStr3[i]) + "\n")
                outputFile.write("\n"+"registers:" + "\n")
                outputFile.write("r00:" + "\t" + "\n"
                                 "r08:" + "\t" + "\n"
                                 "r16:" + "\t" + "\n"
                                 "r24:" + "\t" + "\n")
                outputFile.write("\n" + "data:" + "\n")

            elif team11project2.opcodeStr[i] == "B":
                outputFile.write("====================" + "\n" + "cycle:" + str(i + 1) + " \t " + str(mem_loc)
                                 + " \t" + "B" + "   "+ str(team11project2.argStr1[i]) + "\n")
                outputFile.write("\n"+"registers:" + "\n")
                outputFile.write("r00:" + "\t" + "\n"
                                 "r08:" + "\t" + "\n"
                                 "r16:" + "\t" + "\n"
                                 "r24:" + "\t" + "\n")
                outputFile.write("\n" + "data:" + "\n")

            elif team11project2.opcodeStr[i] == "ADD":
                outputFile.write("====================" + "\n" + "cycle:" + str(i + 1) + " \t " + str(mem_loc)
                                 + " \t" + "ADD" + " " +str(team11project2.argStr1[i]) + ", " +
                                 str(team11project2.argStr2[i]) + ", " + str(team11project2.argStr3[i]) +"\n")
                outputFile.write("\n"+"registers:" + "\n")
                outputFile.write("r00:" + "\t" + "\n"
                                 "r08:" + "\t" + "\n"
                                 "r16:" + "\t" + "\n"
                                 "r24:" + "\t" + "\n")
                outputFile.write("\n" + "data:" + "\n")


            elif team11project2.opcodeStr[i] == "SUB ":
                outputFile.write("====================" + "\n" + "cycle:" + str(i + 1) + " \t " + str(mem_loc)
                                 + " \t" + "SUB" + " "+str(team11project2.argStr1[i]) + ", " +
                                 str(team11project2.argStr2[i]) + ", " + str(team11project2.argStr3[i]) +"\n")
                outputFile.write("\n"+"registers:" + "\n")
                outputFile.write("r00:" + "\t" + "\n"
                                 "r08:" + "\t" + "\n"
                                 "r16:" + "\t" + "\n"
                                 "r24:" + "\t" + "\n")
                outputFile.write("\n" + "data:" + "\n")

            elif team11project2.opcodeStr[i] == "SUBI":
                outputFile.write("====================" + "\n" + "cycle:" + str(i + 1) + " \t " + str(mem_loc)
                                 + " \t" + "SUBI" + " "+ str(team11project2.argStr1[i]) + ", " +
                                 str(team11project2.argStr2[i]) + ", " + str(team11project2.argStr3[i]) +"\n")
                outputFile.write("\n"+"registers:" + "\n")
                outputFile.write("r00:" + "\t" + "\n"
                                 "r08:" + "\t" + "\n"
                                 "r16:" + "\t" + "\n"
                                 "r24:" + "\t" + "\n")
                outputFile.write("\n" + "data:" + "\n")

            elif team11project2.opcodeStr[i] == "AND":
                outputFile.write("====================" + "\n" + "cycle:" + str(i + 1) + " \t " + str(mem_loc)
                                 + " \t" + "AND" + " "+ str(team11project2.argStr1[i]) + ", " +
                                 str(team11project2.argStr2[i]) + ", " + str(team11project2.argStr3[i]) +"\n")
                outputFile.write("\n"+"registers:" + "\n")
                outputFile.write("r00:" + "\t" + "\n"
                                 "r08:" + "\t" + "\n"
                                 "r16:" + "\t" + "\n"
                                 "r24:" + "\t" + "\n")
                outputFile.write("\n" + "data:" + "\n")

            elif team11project2.opcodeStr[i] == "ORR":
                outputFile.write("====================" + "\n" + "cycle:" + str(i + 1) + " \t " + str(mem_loc)
                                 + " \t" + "ORR" + " "+ str(team11project2.argStr1[i]) + ", " +
                                 str(team11project2.argStr2[i]) + ", " + str(team11project2.argStr3[i]) +"\n")
                outputFile.write("\n"+"registers:" + "\n")
                outputFile.write("r00:" + "\t" + "\n"
                                 "r08:" + "\t" + "\n"
                                 "r16:" + "\t" + "\n"
                                 "r24:" + "\t" + "\n")
                outputFile.write("\n" + "data:" + "\n")

            elif team11project2.opcodeStr[i] == "EOR":
                outputFile.write("====================" + "\n" + "cycle:" + str(i + 1) + " \t " + str(mem_loc)
                                 + " \t" + "EOR" + " " + str(team11project2.argStr1[i]) + ", " +
                                 str(team11project2.argStr2[i]) + ", " + str(team11project2.argStr3[i]) +"\n")
                outputFile.write("\n"+"registers:" + "\n")
                outputFile.write("r00:" + "\t" + "\n"
                                 "r08:" + "\t" + "\n"
                                 "r16:" + "\t" + "\n"
                                 "r24:" + "\t" + "\n")
                outputFile.write("\n" + "data:" + "\n")

            elif team11project2.opcodeStr[i] == "MOVZ":
                outputFile.write("====================" + "\n" + "cycle:" + str(i + 1) + " \t " + str(mem_loc)
                                 + " \t" + "MOVZ" + " "+ str(team11project2.argStr1[i]) + ", " +
                                 str(team11project2.argStr2[i]) + ", " + str(team11project2.argStr3[i]) +"\n")
                outputFile.write("\n"+"registers:" + "\n")
                outputFile.write("r00:" + "\t" + "\n"
                                 "r08:" + "\t" + "\n"
                                 "r16:" + "\t" + "\n"
                                 "r24:" + "\t" + "\n")
                outputFile.write("\n" + "data:" + "\n")

            elif team11project2.opcodeStr[i] == "MOVK":
                outputFile.write("====================" + "\n" + "cycle:" + str(i + 1) + " \t " + str(mem_loc)
                                 + " \t" + "MOVK" + " "+ str(team11project2.argStr1[i]) + ", " +
                                 str(team11project2.argStr2[i]) + ", " + str(team11project2.argStr3[i]) +"\n")
                outputFile.write("\n"+"registers:" + "\n")
                outputFile.write("r00:" + "\t" + "\n"
                                 "r08:" + "\t" + "\n"
                                 "r16:" + "\t" + "\n"
                                 "r24:" + "\t" + "\n")
                outputFile.write("\n" + "data:" + "\n")

            elif team11project2.opcodeStr[i] == "STUR":
                outputFile.write("====================" + "\n" + "cycle:" + str(i + 1) + " \t " + str(mem_loc)
                                 + " \t" + "STUR" + " "+ str(team11project2.argStr1[i]) + ", " +
                                 str(team11project2.argStr2[i]) + ", " + str(team11project2.argStr3[i]) +"\n")
                outputFile.write("\n" + "registers:" + "\n")
                outputFile.write("r00:" + "\t" + "\n"
                                 "r08:" + "\t" + "\n"
                                 "r16:" + "\t" + "\n"
                                 "r24:" + "\t" + "\n")
                outputFile.write("\n" + "data:" + "\n")

            elif team11project2.opcodeStr[i] == "LDUR":
                outputFile.write("====================" + "\n" + "cycle:" + str(i + 1) + " \t " + str(mem_loc)
                                 + " \t" + "LDUR" + " "+str(team11project2.argStr1[i]) + ", " +
                                 str(team11project2.argStr2[i]) + ", " + str(team11project2.argStr3[i]) +"\n")
                outputFile.write("\n"+"registers:" + "\n")
                outputFile.write("r00:" + "\t" + "\n"
                                 "r08:" + "\t" + "\n"
                                 "r16:" + "\t" + "\n"
                                 "r24:" + "\t" + "\n")
                outputFile.write("\n" + "data:" + "\n")

            elif team11project2.opcodeStr[i] == "CBZ":
                outputFile.write("====================" + "\n" + "cycle:" + str(i + 1) + " \t " + str(mem_loc)
                                 + " \t" "CBZ" + " "+str(team11project2.argStr1[i]) + ", " +
                                 str(team11project2.argStr2[i]) + ", " + str(team11project2.argStr3[i]) +"\n")
                outputFile.write("\n"+"registers:" + "\n")
                outputFile.write("r00:" + "\t" + "\n"
                                 "r08:" + "\t" + "\n"
                                 "r16:" + "\t" + "\n"
                                 "r24:" + "\t" + "\n")
                outputFile.write("\n" + "data:" + "\n")

            elif team11project2.opcodeStr[i] == "CBNZ":
                outputFile.write("====================" + "\n" + "cycle:" + str(i + 1) + " \t " + str(mem_loc)
                                 + " \t" + "CBNZ" + " "+str(team11project2.argStr1[i]) + ", " +
                                 str(team11project2.argStr2[i]) + ", " + str(team11project2.argStr3[i]) +"\n")
                outputFile.write("\n"+"registers:" + "\n")
                outputFile.write("r00:" + "\t" + "\n"
                                 "r08:" + "\t" + "\n"
                                 "r16:" + "\t" + "\n"
                                 "r24:" + "\t" + "\n")
                outputFile.write("\n" + "data:" + "\n")

            elif team11project2.opcodeStr[i] == "ASR":
                outputFile.write("====================" + "\n" + "cycle:" + str(i + 1) + " \t " + str(mem_loc)
                                 + " \t" + "ASR" + " "+ str(team11project2.argStr1[i]) + ", " +
                                 str(team11project2.argStr2[i]) + ", " + str(team11project2.argStr3[i]) +"\n")
                outputFile.write("\n"+"registers:" + "\n")
                outputFile.write("r00:" + "\t" + "\n"
                                 "r08:" + "\t" + "\n"
                                 "r16:" + "\t" + "\n"
                                 "r24:" + "\t" + "\n")
                outputFile.write("\n" + "data:" + "\n")

            elif team11project2.opcodeStr[i] == "LSL":
                outputFile.write("====================" + "\n" + "cycle:" + str(i + 1) + " \t " + str(mem_loc)
                                 + " \t" + "LSL" + " "+str(team11project2.argStr1[i]) + ", " +
                                 str(team11project2.argStr2[i]) + ", " + str(team11project2.argStr3[i]) +"\n")
                outputFile.write("\n"+"registers:" + "\n")
                outputFile.write("r00:" + "\t" + "\n"
                                 "r08:" + "\t" + "\n"
                                 "r16:" + "\t" + "\n"
                                 "r24:" + "\t" + "\n")
                outputFile.write("\n" + "data:" + "\n")

            elif team11project2.opcodeStr[i] == "LSR":
                outputFile.write("====================" + "\n" + "cycle:" + str(i + 1) + " \t " + str(mem_loc)
                                 + " \t" + "LSR" + " "+ str(team11project2.argStr1[i]) + ", " +
                                 str(team11project2.argStr2[i]) + ", " + str(team11project2.argStr3[i]) +"\n")
                outputFile.write("\n"+"registers:" + "\n")
                outputFile.write("r00:" + "\t" + "\n"
                                 "r08:" + "\t" + "\n"
                                 "r16:" + "\t" + "\n"
                                 "r24:" + "\t" + "\n")
                outputFile.write("\n" + "data:" + "\n")

            elif team11project2.opcodeStr[i] == "NOP":
                outputFile.write("====================" + "\n" + "cycle:" + str(i + 1) + " \t " + str(mem_loc)
                                 + " \t" + "NOP" + "\n")
                outputFile.write("\n"+"registers:" + "\n")
                outputFile.write("r00:" + "\t" + "\n"
                                 "r08:" + "\t" + "\n"
                                 "r16:" + "\t" + "\n"
                                 "r24:" + "\t" + "\n")
                outputFile.write("\n" + "data:" + "\n")

            elif team11project2.opcodeStr[i] == "BREAK":
                outputFile.write("====================" + "\n" + "cycle:" + str(i + 1) + " \t " + str(mem_loc)
                                 + " \t" + "BREAK" + "\n")
                outputFile.write("\n"+"registers:" + "\n")
                outputFile.write("r00:" + "\t" + "\n"
                                 "r08:" + "\t" + "\n"
                                 "r16:" + "\t" + "\n"
                                 "r24:" + "\t" + "\n")
                outputFile.write("\n" + "data:" + "\n")

            print team11project2.opcodeStr[i]
            i += 1
            mem_loc += 4

if __name__ == '__main__':
    test = Simulator()
    test.run()
