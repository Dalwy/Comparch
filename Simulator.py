import disassembler
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
        d = disassembler.TestMe()
        d.run()

        i = 0
        r_32 = [0] * 32
        data_list = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]

        while disassembler.opcodeStr[i] != 'BREAK':
            if disassembler.opcodeStr[i] == "ADDI":
                num = disassembler.arg1[i]
                r_32[int(disassembler.arg3[i])] = r_32[num] + int(disassembler.arg2[i])
                outputFile.write("====================" + "\n" + "cycle:" + str(i + 1) + "\t" + str(Memory)
                                 + "\t" + "ADDI" + "\t" + str(disassembler.argStr1[i]) + "\t" + str(
                    disassembler.argStr2[i])
                                 + "\t" + str(disassembler.argStr3[i]) + "\n")
                outputFile.write("\n" + "registers:" + "\n")
                outputFile.write(
                    "r00: " + str(r_32[0]) + "\t" + str(r_32[1]) + "\t" + str(r_32[2]) + "\t" + str(r_32[3]) + "\t" +
                    str(r_32[4]) + "\t" + str(r_32[5]) + "\t" + str(r_32[6]) + "\t" + str(r_32[7]) + "\t" + "\n" +
                    "r08: " + str(r_32[8]) + "\t" + str(r_32[9]) + "\t" + str(r_32[10]) + "\t" + str(r_32[11]) + "\t" +
                    str(r_32[12]) + "\t" + str(r_32[13]) + "\t" + str(r_32[14]) + "\t" + str(r_32[15]) + "\t" + "\n" +
                    "r16: " + str(r_32[16]) + "\t" + str(r_32[17]) + "\t" + str(r_32[18]) + "\t" + str(
                        r_32[19]) + "\t" +
                    str(r_32[20]) + "\t" + str(r_32[21]) + "\t" + str(r_32[22]) + "\t" + str(r_32[23]) + "\t" + "\n" +
                    "r24: " + str(r_32[24]) + "\t" + str(r_32[25]) + "\t" + str(r_32[26]) + "\t" + str(
                        r_32[27]) + "\t" +
                    str(r_32[28]) + "\t" + str(r_32[29]) + "\t" + str(r_32[30]) + "\t" + str(r_32[31]) + "\t" + "\n")
                outputFile.write("\n" + "data:" + "\n")
            elif disassembler.opcodeStr[i] == "B":
                outputFile.write("====================" + "\n" + "cycle " + str(i + 1) + "\t" + str(Memory)
                                 + "\t" + "B" + "\t" + str(disassembler.argStr1[i]) + "\t" + str(
                    disassembler.argStr2[i])
                                 + "\t" + str(disassembler.argStr3[i]) + "\n")
                outputFile.write("\n" + "registers:" + "\n")
                outputFile.write(
                    "r00: " + str(r_32[0]) + "\t" + str(r_32[1]) + "\t" + str(r_32[2]) + "\t" + str(r_32[3]) + "\t" +
                    str(r_32[4]) + "\t" + str(r_32[5]) + "\t" + str(r_32[6]) + "\t" + str(r_32[7]) + "\t" + "\n" +
                    "r08: " + str(r_32[8]) + "\t" + str(r_32[9]) + "\t" + str(r_32[10]) + "\t" + str(r_32[11]) + "\t" +
                    str(r_32[12]) + "\t" + str(r_32[13]) + "\t" + str(r_32[14]) + "\t" + str(r_32[15]) + "\t" + "\n" +
                    "r16: " + str(r_32[16]) + "\t" + str(r_32[17]) + "\t" + str(r_32[18]) + "\t" + str(
                        r_32[19]) + "\t" +
                    str(r_32[20]) + "\t" + str(r_32[21]) + "\t" + str(r_32[22]) + "\t" + str(r_32[23]) + "\t" + "\n" +
                    "r24: " + str(r_32[24]) + "\t" + str(r_32[25]) + "\t" + str(r_32[26]) + "\t" + str(
                        r_32[27]) + "\t" +
                    str(r_32[28]) + "\t" + str(r_32[29]) + "\t" + str(r_32[30]) + "\t" + str(r_32[31]) + "\t" + "\n")
                outputFile.write("\n" + "data:" + "\n")
            elif disassembler.opcodeStr[i] == "ADD":
                num = disassembler.arg1[i]
                num2 = disassembler.arg2[i]
                r_32[disassembler.arg3[i]] = r_32[num] + r_32[num2]
                outputFile.write("====================" + "\n" + "cycle " + str(i + 1) + "\t" + str(Memory)
                                 + "\t" + "ADD" + "\t" + str(disassembler.argStr1[i]) + "\t" + str(
                    disassembler.argStr2[i])
                                 + "\t" + str(disassembler.argStr3[i]) + "\n")
                outputFile.write("\n" + "registers:" + "\n")
                outputFile.write(
                    "r00: " + str(r_32[0]) + "\t" + str(r_32[1]) + "\t" + str(r_32[2]) + "\t" + str(r_32[3]) + "\t" +
                    str(r_32[4]) + "\t" + str(r_32[5]) + "\t" + str(r_32[6]) + "\t" + str(r_32[7]) + "\t" + "\n" +
                    "r08: " + str(r_32[8]) + "\t" + str(r_32[9]) + "\t" + str(r_32[10]) + "\t" + str(r_32[11]) + "\t" +
                    str(r_32[12]) + "\t" + str(r_32[13]) + "\t" + str(r_32[14]) + "\t" + str(r_32[15]) + "\t" + "\n" +
                    "r16: " + str(r_32[16]) + "\t" + str(r_32[17]) + "\t" + str(r_32[18]) + "\t" + str(
                        r_32[19]) + "\t" +
                    str(r_32[20]) + "\t" + str(r_32[21]) + "\t" + str(r_32[22]) + "\t" + str(r_32[23]) + "\t" + "\n" +
                    "r24: " + str(r_32[24]) + "\t" + str(r_32[25]) + "\t" + str(r_32[26]) + "\t" + str(
                        r_32[27]) + "\t" +
                    str(r_32[28]) + "\t" + str(r_32[29]) + "\t" + str(r_32[30]) + "\t" + str(r_32[31]) + "\t" + "\n")
            elif disassembler.opcodeStr[i] == "SUB":
                num = disassembler.arg1[i]
                num2 = disassembler.arg2[i]
                r_32[disassembler.arg3[i]] = r_32[num] - r_32[num2]
                outputFile.write("====================" + "\n" + "cycle " + str(i + 1) + "\t" + str(Memory)
                                 + "\t" + "SUB" + "\t" + str(disassembler.argStr1[i]) + "\t" + str(
                    disassembler.argStr2[i])
                                 + "\t" + str(disassembler.argStr3[i]) + "\n")
                outputFile.write("\n" + "registers:" + "\n")
                outputFile.write(
                    "r00: " + str(r_32[0]) + "\t" + str(r_32[1]) + "\t" + str(r_32[2]) + "\t" + str(r_32[3]) + "\t" +
                    str(r_32[4]) + "\t" + str(r_32[5]) + "\t" + str(r_32[6]) + "\t" + str(r_32[7]) + "\t" + "\n" +
                    "r08: " + str(r_32[8]) + "\t" + str(r_32[9]) + "\t" + str(r_32[10]) + "\t" + str(r_32[11]) + "\t" +
                    str(r_32[12]) + "\t" + str(r_32[13]) + "\t" + str(r_32[14]) + "\t" + str(r_32[15]) + "\t" + "\n" +
                    "r16: " + str(r_32[16]) + "\t" + str(r_32[17]) + "\t" + str(r_32[18]) + "\t" + str(
                        r_32[19]) + "\t" +
                    str(r_32[20]) + "\t" + str(r_32[21]) + "\t" + str(r_32[22]) + "\t" + str(r_32[23]) + "\t" + "\n" +
                    "r24: " + str(r_32[24]) + "\t" + str(r_32[25]) + "\t" + str(r_32[26]) + "\t" + str(
                        r_32[27]) + "\t" +
                    str(r_32[28]) + "\t" + str(r_32[29]) + "\t" + str(r_32[30]) + "\t" + str(r_32[31]) + "\t" + "\n")
                outputFile.write("\n" + "data:" + "\n")
            elif disassembler.opcodeStr[i] == "SUBI":
                num = disassembler.arg1[i]
                r_32[int(disassembler.arg3[i])] = r_32[num] - int(disassembler.arg2[i])
                outputFile.write("====================" + "\n" + "cycle " + str(i + 1) + "\t" + str(Memory)
                                 + "\t" + "SUBI" + "\t" + str(disassembler.argStr1[i]) + "\t" + str(
                    disassembler.argStr2[i])
                                 + "\t" + str(disassembler.argStr3[i]) + "\n")
                outputFile.write("\n" + "registers:" + "\n")
                outputFile.write(
                    "r00: " + str(r_32[0]) + "\t" + str(r_32[1]) + "\t" + str(r_32[2]) + "\t" + str(r_32[3]) + "\t" +
                    str(r_32[4]) + "\t" + str(r_32[5]) + "\t" + str(r_32[6]) + "\t" + str(r_32[7]) + "\t" + "\n" +
                    "r08: " + str(r_32[8]) + "\t" + str(r_32[9]) + "\t" + str(r_32[10]) + "\t" + str(r_32[11]) + "\t" +
                    str(r_32[12]) + "\t" + str(r_32[13]) + "\t" + str(r_32[14]) + "\t" + str(r_32[15]) + "\t" + "\n" +
                    "r16: " + str(r_32[16]) + "\t" + str(r_32[17]) + "\t" + str(r_32[18]) + "\t" + str(
                        r_32[19]) + "\t" +
                    str(r_32[20]) + "\t" + str(r_32[21]) + "\t" + str(r_32[22]) + "\t" + str(r_32[23]) + "\t" + "\n" +
                    "r24: " + str(r_32[24]) + "\t" + str(r_32[25]) + "\t" + str(r_32[26]) + "\t" + str(
                        r_32[27]) + "\t" +
                    str(r_32[28]) + "\t" + str(r_32[29]) + "\t" + str(r_32[30]) + "\t" + str(r_32[31]) + "\t" + "\n")
                outputFile.write("\n" + "data:" + "\n")
            elif disassembler.opcodeStr[i] == "AND":
                outputFile.write("====================" + "\n" + "cycle " + str(i + 1) + "\t" + str(Memory)
                                 + "\t" + "AND" + "\t" + str(disassembler.argStr1[i]) + "\t" + str(
                    disassembler.argStr2[i])
                                 + "\t" + str(disassembler.argStr3[i]) + "\n")
                outputFile.write("\n" + "registers:" + "\n")
                outputFile.write(
                    "r00: " + str(r_32[0]) + "\t" + str(r_32[1]) + "\t" + str(r_32[2]) + "\t" + str(r_32[3]) + "\t" +
                    str(r_32[4]) + "\t" + str(r_32[5]) + "\t" + str(r_32[6]) + "\t" + str(r_32[7]) + "\t" + "\n" +
                    "r08: " + str(r_32[8]) + "\t" + str(r_32[9]) + "\t" + str(r_32[10]) + "\t" + str(r_32[11]) + "\t" +
                    str(r_32[12]) + "\t" + str(r_32[13]) + "\t" + str(r_32[14]) + "\t" + str(r_32[15]) + "\t" + "\n" +
                    "r16: " + str(r_32[16]) + "\t" + str(r_32[17]) + "\t" + str(r_32[18]) + "\t" + str(
                        r_32[19]) + "\t" +
                    str(r_32[20]) + "\t" + str(r_32[21]) + "\t" + str(r_32[22]) + "\t" + str(r_32[23]) + "\t" + "\n" +
                    "r24: " + str(r_32[24]) + "\t" + str(r_32[25]) + "\t" + str(r_32[26]) + "\t" + str(
                        r_32[27]) + "\t" +
                    str(r_32[28]) + "\t" + str(r_32[29]) + "\t" + str(r_32[30]) + "\t" + str(r_32[31]) + "\t" + "\n")
                outputFile.write("\n" + "data:" + "\n")
            elif disassembler.opcodeStr[i] == "ORR":
                outputFile.write("====================" + "\n" + "cycle " + str(i + 1) + "\t" + str(Memory)
                                 + "\t" + "ORR" + "\t" + str(disassembler.argStr1[i]) + "\t" + str(
                    disassembler.argStr2[i])
                                 + "\t" + str(disassembler.argStr3[i]) + "\n")
                outputFile.write("\n" + "registers:" + "\n")
                outputFile.write(
                    "r00: " + str(r_32[0]) + "\t" + str(r_32[1]) + "\t" + str(r_32[2]) + "\t" + str(r_32[3]) + "\t" +
                    str(r_32[4]) + "\t" + str(r_32[5]) + "\t" + str(r_32[6]) + "\t" + str(r_32[7]) + "\t" + "\n" +
                    "r08: " + str(r_32[8]) + "\t" + str(r_32[9]) + "\t" + str(r_32[10]) + "\t" + str(r_32[11]) + "\t" +
                    str(r_32[12]) + "\t" + str(r_32[13]) + "\t" + str(r_32[14]) + "\t" + str(r_32[15]) + "\t" + "\n" +
                    "r16: " + str(r_32[16]) + "\t" + str(r_32[17]) + "\t" + str(r_32[18]) + "\t" + str(
                        r_32[19]) + "\t" +
                    str(r_32[20]) + "\t" + str(r_32[21]) + "\t" + str(r_32[22]) + "\t" + str(r_32[23]) + "\t" + "\n" +
                    "r24: " + str(r_32[24]) + "\t" + str(r_32[25]) + "\t" + str(r_32[26]) + "\t" + str(
                        r_32[27]) + "\t" +
                    str(r_32[28]) + "\t" + str(r_32[29]) + "\t" + str(r_32[30]) + "\t" + str(r_32[31]) + "\t" + "\n")
                outputFile.write("\n" + "data:" + "\n")
            elif disassembler.opcodeStr[i] == "EOR":
                outputFile.write("====================" + "\n" + "cycle " + str(i + 1) + "\t" + str(Memory)
                                 + "\t" + "EOR" + "\t" + str(disassembler.argStr1[i]) + "\t" + str(
                    disassembler.argStr2[i])
                                 + "\t" + str(disassembler.argStr3[i]) + "\n")
                outputFile.write("\n" + "registers:" + "\n")
                outputFile.write(
                    "r00: " + str(r_32[0]) + "\t" + str(r_32[1]) + "\t" + str(r_32[2]) + "\t" + str(r_32[3]) + "\t" +
                    str(r_32[4]) + "\t" + str(r_32[5]) + "\t" + str(r_32[6]) + "\t" + str(r_32[7]) + "\t" + "\n" +
                    "r08: " + str(r_32[8]) + "\t" + str(r_32[9]) + "\t" + str(r_32[10]) + "\t" + str(r_32[11]) + "\t" +
                    str(r_32[12]) + "\t" + str(r_32[13]) + "\t" + str(r_32[14]) + "\t" + str(r_32[15]) + "\t" + "\n" +
                    "r16: " + str(r_32[16]) + "\t" + str(r_32[17]) + "\t" + str(r_32[18]) + "\t" + str(
                        r_32[19]) + "\t" +
                    str(r_32[20]) + "\t" + str(r_32[21]) + "\t" + str(r_32[22]) + "\t" + str(r_32[23]) + "\t" + "\n" +
                    "r24: " + str(r_32[24]) + "\t" + str(r_32[25]) + "\t" + str(r_32[26]) + "\t" + str(
                        r_32[27]) + "\t" +
                    str(r_32[28]) + "\t" + str(r_32[29]) + "\t" + str(r_32[30]) + "\t" + str(r_32[31]) + "\t" + "\n")
                outputFile.write("\n" + "data:" + "\n")
            elif disassembler.opcodeStr[i] == "MOVZ":
                outputFile.write("====================" + "\n" + "cycle " + str(i + 1) + "\t" + str(Memory)
                                 + "\t" + "MOVZ" + "\t" + str(disassembler.argStr1[i]) + "\t" + str(
                    disassembler.argStr3[i])
                                 + "\t" + str(disassembler.argStr2[i]) + "\n")
                outputFile.write("\n" + "registers:" + "\n")
                outputFile.write(
                    "r00: " + str(r_32[0]) + "\t" + str(r_32[1]) + "\t" + str(r_32[2]) + "\t" + str(r_32[3]) + "\t" +
                    str(r_32[4]) + "\t" + str(r_32[5]) + "\t" + str(r_32[6]) + "\t" + str(r_32[7]) + "\t" + "\n" +
                    "r08: " + str(r_32[8]) + "\t" + str(r_32[9]) + "\t" + str(r_32[10]) + "\t" + str(r_32[11]) + "\t" +
                    str(r_32[12]) + "\t" + str(r_32[13]) + "\t" + str(r_32[14]) + "\t" + str(r_32[15]) + "\t" + "\n" +
                    "r16: " + str(r_32[16]) + "\t" + str(r_32[17]) + "\t" + str(r_32[18]) + "\t" + str(
                        r_32[19]) + "\t" +
                    str(r_32[20]) + "\t" + str(r_32[21]) + "\t" + str(r_32[22]) + "\t" + str(r_32[23]) + "\t" + "\n" +
                    "r24: " + str(r_32[24]) + "\t" + str(r_32[25]) + "\t" + str(r_32[26]) + "\t" + str(
                        r_32[27]) + "\t" +
                    str(r_32[28]) + "\t" + str(r_32[29]) + "\t" + str(r_32[30]) + "\t" + str(r_32[31]) + "\t" + "\n")
                outputFile.write("\n" + "data:" + "\n")
            elif disassembler.opcodeStr[i] == "MOVK":
                outputFile.write("====================" + "\n" + "cycle " + str(i + 1) + "\t" + str(Memory)
                                 + "\t" + "MOVK" + "\t" + str(disassembler.argStr1[i]) + "\t" + str(
                    disassembler.argStr3[i])
                                 + "\t" + str(disassembler.argStr2[i]) + "\n")
                outputFile.write("\n" + "registers:" + "\n")
                outputFile.write(
                    "r00: " + str(r_32[0]) + "\t" + str(r_32[1]) + "\t" + str(r_32[2]) + "\t" + str(r_32[3]) + "\t" +
                    str(r_32[4]) + "\t" + str(r_32[5]) + "\t" + str(r_32[6]) + "\t" + str(r_32[7]) + "\t" + "\n" +
                    "r08: " + str(r_32[8]) + "\t" + str(r_32[9]) + "\t" + str(r_32[10]) + "\t" + str(r_32[11]) + "\t" +
                    str(r_32[12]) + "\t" + str(r_32[13]) + "\t" + str(r_32[14]) + "\t" + str(r_32[15]) + "\t" + "\n" +
                    "r16: " + str(r_32[16]) + "\t" + str(r_32[17]) + "\t" + str(r_32[18]) + "\t" + str(
                        r_32[19]) + "\t" +
                    str(r_32[20]) + "\t" + str(r_32[21]) + "\t" + str(r_32[22]) + "\t" + str(r_32[23]) + "\t" + "\n" +
                    "r24: " + str(r_32[24]) + "\t" + str(r_32[25]) + "\t" + str(r_32[26]) + "\t" + str(
                        r_32[27]) + "\t" +
                    str(r_32[28]) + "\t" + str(r_32[29]) + "\t" + str(r_32[30]) + "\t" + str(r_32[31]) + "\t" + "\n")
                outputFile.write("\n" + "data:" + "\n")
            elif disassembler.opcodeStr[i] == "STUR":
                store = disassembler.arg3[i]
                addr = disassembler.arg1[i] + disassembler.arg2[i] * 4
                outputFile.write("====================" + "\n" + "cycle " + str(i + 1) + "\t" + str(Memory)
                                 + "\t" + "STUR" + "\t" + str(disassembler.argStr1[i]) + "\t" + str(
                    disassembler.argStr2[i])
                                 + "\t" + str(disassembler.argStr3[i]) + "\n")
                outputFile.write("\n" + "registers:" + "\n")
                outputFile.write(
                    "r00: " + str(r_32[0]) + "\t" + str(r_32[1]) + "\t" + str(r_32[2]) + "\t" + str(r_32[3]) + "\t" +
                    str(r_32[4]) + "\t" + str(r_32[5]) + "\t" + str(r_32[6]) + "\t" + str(r_32[7]) + "\t" + "\n" +
                    "r08: " + str(r_32[8]) + "\t" + str(r_32[9]) + "\t" + str(r_32[10]) + "\t" + str(r_32[11]) + "\t" +
                    str(r_32[12]) + "\t" + str(r_32[13]) + "\t" + str(r_32[14]) + "\t" + str(r_32[15]) + "\t" + "\n" +
                    "r16: " + str(r_32[16]) + "\t" + str(r_32[17]) + "\t" + str(r_32[18]) + "\t" + str(
                        r_32[19]) + "\t" +
                    str(r_32[20]) + "\t" + str(r_32[21]) + "\t" + str(r_32[22]) + "\t" + str(r_32[23]) + "\t" + "\n" +
                    "r24: " + str(r_32[24]) + "\t" + str(r_32[25]) + "\t" + str(r_32[26]) + "\t" + str(
                        r_32[27]) + "\t" +
                    str(r_32[28]) + "\t" + str(r_32[29]) + "\t" + str(r_32[30]) + "\t" + str(r_32[31]) + "\t" + "\n")

                outputFile.write("\n" + "data:" + "\n")
                data_start = disassembler.Memory + 4
                data_rows = [data_start, data_start + 32, data_start + 64, data_start + 96]

                while addr > data_rows[-1]:
                    data_rows.append(data_rows[-1] + 32)
                    data_list.append([0, 0, 0, 0, 0, 0, 0, 0])

                for i in range(len(data_rows)):
                    if addr > data_rows[i]:
                        continue
                    elif addr < data_rows[i]:
                        row_index = i - 1
                        data_index = (addr - data_rows[row_index]) / 4
                        data_list[row_index][data_index] = store

                for row, data in data_rows, data_list:
                    outputFile.write(str(row) + ": " + str(data))

            elif disassembler.opcodeStr[i] == "LDUR":
                outputFile.write("====================" + "\n" + "cycle " + str(i + 1) + "\t" + str(Memory)
                                 + "\t" + "LDUR" + "\t" + str(disassembler.argStr1[i]) + "\t" + str(
                    disassembler.argStr2[i])
                                 + "\t" + str(disassembler.argStr3[i]) + "\n")
                outputFile.write("\n" + "registers:" + "\n")
                outputFile.write(
                    "r00: " + str(r_32[0]) + "\t" + str(r_32[1]) + "\t" + str(r_32[2]) + "\t" + str(r_32[3]) + "\t" +
                    str(r_32[4]) + "\t" + str(r_32[5]) + "\t" + str(r_32[6]) + "\t" + str(r_32[7]) + "\t" + "\n" +
                    "r08: " + str(r_32[8]) + "\t" + str(r_32[9]) + "\t" + str(r_32[10]) + "\t" + str(r_32[11]) + "\t" +
                    str(r_32[12]) + "\t" + str(r_32[13]) + "\t" + str(r_32[14]) + "\t" + str(r_32[15]) + "\t" + "\n" +
                    "r16: " + str(r_32[16]) + "\t" + str(r_32[17]) + "\t" + str(r_32[18]) + "\t" + str(
                        r_32[19]) + "\t" +
                    str(r_32[20]) + "\t" + str(r_32[21]) + "\t" + str(r_32[22]) + "\t" + str(r_32[23]) + "\t" + "\n" +
                    "r24: " + str(r_32[24]) + "\t" + str(r_32[25]) + "\t" + str(r_32[26]) + "\t" + str(
                        r_32[27]) + "\t" +
                    str(r_32[28]) + "\t" + str(r_32[29]) + "\t" + str(r_32[30]) + "\t" + str(r_32[31]) + "\t" + "\n")
                outputFile.write("\n" + "data:" + "\n")
            elif disassembler.opcodeStr[i] == "CBZ":
                outputFile.write("====================" + "\n" + "cycle " + str(i + 1) + "\t" + str(Memory)
                                 + "\t" "CBZ" + "\t" + str(disassembler.argStr1[i]) + "\t" + str(
                    disassembler.argStr2[i])
                                 + "\t" + str(disassembler.argStr3[i]) + "\n")
                outputFile.write("\n" + "registers:" + "\n")
                outputFile.write(
                    "r00: " + str(r_32[0]) + "\t" + str(r_32[1]) + "\t" + str(r_32[2]) + "\t" + str(r_32[3]) + "\t" +
                    str(r_32[4]) + "\t" + str(r_32[5]) + "\t" + str(r_32[6]) + "\t" + str(r_32[7]) + "\t" + "\n" +
                    "r08: " + str(r_32[8]) + "\t" + str(r_32[9]) + "\t" + str(r_32[10]) + "\t" + str(r_32[11]) + "\t" +
                    str(r_32[12]) + "\t" + str(r_32[13]) + "\t" + str(r_32[14]) + "\t" + str(r_32[15]) + "\t" + "\n" +
                    "r16: " + str(r_32[16]) + "\t" + str(r_32[17]) + "\t" + str(r_32[18]) + "\t" + str(
                        r_32[19]) + "\t" +
                    str(r_32[20]) + "\t" + str(r_32[21]) + "\t" + str(r_32[22]) + "\t" + str(r_32[23]) + "\t" + "\n" +
                    "r24: " + str(r_32[24]) + "\t" + str(r_32[25]) + "\t" + str(r_32[26]) + "\t" + str(
                        r_32[27]) + "\t" +
                    str(r_32[28]) + "\t" + str(r_32[29]) + "\t" + str(r_32[30]) + "\t" + str(r_32[31]) + "\t" + "\n")
                outputFile.write("\n" + "data:" + "\n")
            elif disassembler.opcodeStr[i] == "CBNZ":
                outputFile.write("====================" + "\n" + "cycle " + str(i + 1) + "\t" + str(Memory)
                                 + "\t" + "CBNZ" + "\t" + str(disassembler.argStr1[i]) + "\t" + str(
                    disassembler.argStr2[i])
                                 + "\t" + str(disassembler.argStr3[i]) + "\n")
                outputFile.write("\n" + "registers:" + "\n")
                outputFile.write(
                    "r00: " + str(r_32[0]) + "\t" + str(r_32[1]) + "\t" + str(r_32[2]) + "\t" + str(r_32[3]) + "\t" +
                    str(r_32[4]) + "\t" + str(r_32[5]) + "\t" + str(r_32[6]) + "\t" + str(r_32[7]) + "\t" + "\n" +
                    "r08: " + str(r_32[8]) + "\t" + str(r_32[9]) + "\t" + str(r_32[10]) + "\t" + str(r_32[11]) + "\t" +
                    str(r_32[12]) + "\t" + str(r_32[13]) + "\t" + str(r_32[14]) + "\t" + str(r_32[15]) + "\t" + "\n" +
                    "r16: " + str(r_32[16]) + "\t" + str(r_32[17]) + "\t" + str(r_32[18]) + "\t" + str(
                        r_32[19]) + "\t" +
                    str(r_32[20]) + "\t" + str(r_32[21]) + "\t" + str(r_32[22]) + "\t" + str(r_32[23]) + "\t" + "\n" +
                    "r24: " + str(r_32[24]) + "\t" + str(r_32[25]) + "\t" + str(r_32[26]) + "\t" + str(
                        r_32[27]) + "\t" +
                    str(r_32[28]) + "\t" + str(r_32[29]) + "\t" + str(r_32[30]) + "\t" + str(r_32[31]) + "\t" + "\n")
                outputFile.write("\n" + "data:" + "\n")
            elif disassembler.opcodeStr[i] == "ASR":
                outputFile.write("====================" + "\n" + "cycle " + str(i + 1) + "\t" + str(Memory)
                                 + "\t" + "ASR" + "\t" + str(disassembler.argStr1[i]) + "\t" + str(
                    disassembler.argStr2[i])
                                 + "\t" + str(disassembler.argStr3[i]) + "\n")
                outputFile.write("\n" + "registers:" + "\n")
                outputFile.write(
                    "r00: " + str(r_32[0]) + "\t" + str(r_32[1]) + "\t" + str(r_32[2]) + "\t" + str(r_32[3]) + "\t" +
                    str(r_32[4]) + "\t" + str(r_32[5]) + "\t" + str(r_32[6]) + "\t" + str(r_32[7]) + "\t" + "\n" +
                    "r08: " + str(r_32[8]) + "\t" + str(r_32[9]) + "\t" + str(r_32[10]) + "\t" + str(r_32[11]) + "\t" +
                    str(r_32[12]) + "\t" + str(r_32[13]) + "\t" + str(r_32[14]) + "\t" + str(r_32[15]) + "\t" + "\n" +
                    "r16: " + str(r_32[16]) + "\t" + str(r_32[17]) + "\t" + str(r_32[18]) + "\t" + str(
                        r_32[19]) + "\t" +
                    str(r_32[20]) + "\t" + str(r_32[21]) + "\t" + str(r_32[22]) + "\t" + str(r_32[23]) + "\t" + "\n" +
                    "r24: " + str(r_32[24]) + "\t" + str(r_32[25]) + "\t" + str(r_32[26]) + "\t" + str(
                        r_32[27]) + "\t" +
                    str(r_32[28]) + "\t" + str(r_32[29]) + "\t" + str(r_32[30]) + "\t" + str(r_32[31]) + "\t" + "\n")
                outputFile.write("\n" + "data:" + "\n")
            elif disassembler.opcodeStr[i] == "LSL ":
                outputFile.write("====================" + "\n" + "cycle " + str(i + 1) + "\t" + str(Memory)
                                 + "\t" + "LSL" + "\t" + str(disassembler.argStr1[i]) + "\t" + str(
                    disassembler.argStr2[i])
                                 + "\t" + str(disassembler.argStr3[i]) + "\n")
                outputFile.write("\n" + "registers:" + "\n")
                outputFile.write(
                    "r00: " + str(r_32[0]) + "\t" + str(r_32[1]) + "\t" + str(r_32[2]) + "\t" + str(r_32[3]) + "\t" +
                    str(r_32[4]) + "\t" + str(r_32[5]) + "\t" + str(r_32[6]) + "\t" + str(r_32[7]) + "\t" + "\n" +
                    "r08: " + str(r_32[8]) + "\t" + str(r_32[9]) + "\t" + str(r_32[10]) + "\t" + str(r_32[11]) + "\t" +
                    str(r_32[12]) + "\t" + str(r_32[13]) + "\t" + str(r_32[14]) + "\t" + str(r_32[15]) + "\t" + "\n" +
                    "r16: " + str(r_32[16]) + "\t" + str(r_32[17]) + "\t" + str(r_32[18]) + "\t" + str(
                        r_32[19]) + "\t" +
                    str(r_32[20]) + "\t" + str(r_32[21]) + "\t" + str(r_32[22]) + "\t" + str(r_32[23]) + "\t" + "\n" +
                    "r24: " + str(r_32[24]) + "\t" + str(r_32[25]) + "\t" + str(r_32[26]) + "\t" + str(
                        r_32[27]) + "\t" +
                    str(r_32[28]) + "\t" + str(r_32[29]) + "\t" + str(r_32[30]) + "\t" + str(r_32[31]) + "\t" + "\n")
                outputFile.write("\n" + "data:" + "\n")
            elif disassembler.opcodeStr[i] == "LSR ":
                outputFile.write("====================" + "\n" + "cycle " + str(i + 1) + "\t" + str(Memory)
                                 + "\t" + "LSR" + "\t" + str(disassembler.argStr1[i]) + "\t" + str(
                    disassembler.argStr2[i])
                                 + "\t" + str(disassembler.argStr3[i]) + "\n")
                outputFile.write("\n" + "registers:" + "\n")
                outputFile.write(
                    "r00: " + str(r_32[0]) + "\t" + str(r_32[1]) + "\t" + str(r_32[2]) + "\t" + str(r_32[3]) + "\t" +
                    str(r_32[4]) + "\t" + str(r_32[5]) + "\t" + str(r_32[6]) + "\t" + str(r_32[7]) + "\t" + "\n" +
                    "r08: " + str(r_32[8]) + "\t" + str(r_32[9]) + "\t" + str(r_32[10]) + "\t" + str(r_32[11]) + "\t" +
                    str(r_32[12]) + "\t" + str(r_32[13]) + "\t" + str(r_32[14]) + "\t" + str(r_32[15]) + "\t" + "\n" +
                    "r16: " + str(r_32[16]) + "\t" + str(r_32[17]) + "\t" + str(r_32[18]) + "\t" + str(
                        r_32[19]) + "\t" +
                    str(r_32[20]) + "\t" + str(r_32[21]) + "\t" + str(r_32[22]) + "\t" + str(r_32[23]) + "\t" + "\n" +
                    "r24: " + str(r_32[24]) + "\t" + str(r_32[25]) + "\t" + str(r_32[26]) + "\t" + str(
                        r_32[27]) + "\t" +
                    str(r_32[28]) + "\t" + str(r_32[29]) + "\t" + str(r_32[30]) + "\t" + str(r_32[31]) + "\t" + "\n")
                outputFile.write("\n" + "data:" + "\n")
            elif disassembler.opcodeStr[i] == "NOP":
                outputFile.write("====================" + "\n" + "cycle " + str(i + 1) + "\t" + str(Memory)
                                 + "\t" + "NOP" + "\n")
                outputFile.write("\n" + "registers:" + "\n")
                outputFile.write(
                    "r00: " + str(r_32[0]) + "\t" + str(r_32[1]) + "\t" + str(r_32[2]) + "\t" + str(r_32[3]) + "\t" +
                    str(r_32[4]) + "\t" + str(r_32[5]) + "\t" + str(r_32[6]) + "\t" + str(r_32[7]) + "\t" + "\n" +
                    "r08: " + str(r_32[8]) + "\t" + str(r_32[9]) + "\t" + str(r_32[10]) + "\t" + str(r_32[11]) + "\t" +
                    str(r_32[12]) + "\t" + str(r_32[13]) + "\t" + str(r_32[14]) + "\t" + str(r_32[15]) + "\t" + "\n" +
                    "r16: " + str(r_32[16]) + "\t" + str(r_32[17]) + "\t" + str(r_32[18]) + "\t" + str(
                        r_32[19]) + "\t" +
                    str(r_32[20]) + "\t" + str(r_32[21]) + "\t" + str(r_32[22]) + "\t" + str(r_32[23]) + "\t" + "\n" +
                    "r24: " + str(r_32[24]) + "\t" + str(r_32[25]) + "\t" + str(r_32[26]) + "\t" + str(
                        r_32[27]) + "\t" +
                    str(r_32[28]) + "\t" + str(r_32[29]) + "\t" + str(r_32[30]) + "\t" + str(r_32[31]) + "\t" + "\n")
                outputFile.write("\n" + "data:" + "\n")
            elif disassembler.opcodeStr[i] == "BREAK":
                outputFile.write("====================" + "\n" + "cycle: " + str(i + 1) + "\t" + str(Memory)
                                 + "\t" + "BREAK" + "\n")
                outputFile.write("\n" + "registers:" + "\n")
                outputFile.write(
                    "r00: " + str(r_32[0]) + "\t" + str(r_32[1]) + "\t" + str(r_32[2]) + "\t" + str(r_32[3]) + "\t" +
                    str(r_32[4]) + "\t" + str(r_32[5]) + "\t" + str(r_32[6]) + "\t" + str(r_32[7]) + "\t" + "\n" +
                    "r08: " + str(r_32[8]) + "\t" + str(r_32[9]) + "\t" + str(r_32[10]) + "\t" + str(r_32[11]) + "\t" +
                    str(r_32[12]) + "\t" + str(r_32[13]) + "\t" + str(r_32[14]) + "\t" + str(r_32[15]) + "\t" + "\n" +
                    "r16: " + str(r_32[16]) + "\t" + str(r_32[17]) + "\t" + str(r_32[18]) + "\t" + str(
                        r_32[19]) + "\t" +
                    str(r_32[20]) + "\t" + str(r_32[21]) + "\t" + str(r_32[22]) + "\t" + str(r_32[23]) + "\t" + "\n" +
                    "r24: " + str(r_32[24]) + "\t" + str(r_32[25]) + "\t" + str(r_32[26]) + "\t" + str(
                        r_32[27]) + "\t" +
                    str(r_32[28]) + "\t" + str(r_32[29]) + "\t" + str(r_32[30]) + "\t" + str(r_32[31]) + "\t" + "\n")
                outputFile.write("\n" + "data:" + "\n")
            i += 1
            Memory += 4


if __name__ == '__main__':
    test = Simulator()
    test.run()


