import team12_Disassembler
import sys

cycle = 0
pre_issue_buff = [-1, -1, -1, -1]
pre_issue_buff2 = [-1, -1, -1, -1]
pre_alu_buff = [-1, -1]
pre_mem_buff = [-1, -1]
post_mem_buff = [-1, -1]
post_alu_buff = [-1]
r = [0] * 32
op = []


class Pipeline:
    class WB:

        def __init__(self):
            pass

        @staticmethod
        def run():

            if post_alu_buff[0] != -1:
                r[post_alu_buff[1]] = post_alu_buff[0]
                post_alu_buff[0] = -1
                post_alu_buff[1] = -1
            if post_mem_buff[0] != -1:
                r[post_mem_buff[1]] = post_mem_buff[0]
                post_mem_buff[0] = -1
                post_mem_buff[1] = -1

    def __init__(self, instrs, opcodes, mem, addrs,
                 arg1, arg2, arg3, num_instrs, dest, src1, src2, cycle):
        self.instrs = instrs
        self.opcodes = opcodes
        self.mem = mem
        self.addrs = addrs
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3
        self.num_instrs = num_instrs
        self.dest = dest
        self.src1 = src1
        self.src2 = src2
        self.cycle = cycle

    def print_state(self, output_file):
        for i in range(len(team12_Disassembler.instructions)):
            output_file.write( "\nCycle: " + str( i+1 ) + "\n" )
            output_file.write( "Pre-Issue Buffer:" + "\n" )
            # print pre_issue_buff
            for i in range( len( pre_issue_buff ) ):
                output_file.write( "Entry " + str( i ) + ":\t" + str( pre_issue_buff[i] ) + "\n" )
            output_file.write( "Pre_ALU Queue:" + "\n" )
            for i in range( len( pre_alu_buff ) ):
                output_file.write( "Entry " + str( i ) + ":" + str( pre_alu_buff[i] ) + "\n" )
            output_file.write( "Post_ALU Queue:" + "\n" )
            for i in range( len( post_alu_buff ) ):
                output_file.write( "Entry " + str( i ) + ":" + str( post_alu_buff[i] ) + "\n" )
            output_file.write( "Pre_MEM Queue:" + "\n" )
            for i in range( len( pre_mem_buff ) ):
                output_file.write( "Entry " + str( i ) + ":" + str( pre_mem_buff[i] ) + "\n" )
            output_file.write( "Post_MEM Queue:" + "\n" )
            for i in range( len( post_mem_buff ) ):
                output_file.write( "Entry " + str( i ) + ":" + str( post_mem_buff[i] ) + "\n" )
            output_file.write( "Registers:" + "\n" )
            output_file.write( "R00:" + "\t")

            for i in range( len( r ) ):
                if i == 8 or i == 16 or i == 24:
                    output_file.write( "\n" )
                    if i == 8:
                        output_file.write( "R0" + str( i ) + ":\t" )
                    else:
                        output_file.write( "R" + str( i ) + ":\t" )
                output_file.write( str( r[i] ) + "\t" )

    def run(self):

        for i in range(len(sys.argv)):
            if sys.argv[i] == '-i' and i < (len( sys.argv ) - 1):
                input_file = sys.argv[i + i]
            elif sys.argv[i] == '-o' and i < (len( sys.argv ) - 1):
                output_file = sys.argv[i + 1]

        output_file = open(output_file + "_sim.txt", 'w' )

        tester = True
        while tester:
            self.WB.run()
            self.Fetch.run(self)
            self.ALU.run(self)
            self.print_state(output_file)
            self.cycle += 1
            tester = False
    # class IssueBuffer:
    #
    #     def __init__(self):
    #         pass
    #
    #     @staticmethod
    #     def run():
    #         if post_alu_buff[1] != 1:
    #             if Pipeline.src1[i] == Pipeline.dest[post_alu_buff[1]] or Pipeline.src2[i] == Pipeline.dest[post_alu_buff[1]]:
    #                 issueMe = False
    #                 if Pipeline.src1[i] == Pipeline.dest[post_mem_buff[1]] or Pipeline.src2[i] == Pipeline.dest[post_mem_buff[1]]:
    #                     issueMe = False
    #         print ("UNDER CONSTRUCTION")


    class MEM:

        def __init__(self):
            pass

        @staticmethod
        def run():
            print("Do the damn thing")

    # class Cache:
    #
    #     sets = [[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0]], [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0]],
    #             [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0]], [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]]
    #
    #     lru = [0, 0, 0, 0]
    #     tag_msk = 4294967264
    #     set_msk = 24
    #
    #     missed_list = []
    #
    #     def __init__(self):
    #         pass
    #
    #     @staticmethod
    #     def flush():
    #         print("Flush, bitch")
    #
    #     @staticmethod
    #     def access_mem(mem_idx, inst_idx, is_write, data_to_write):
    #         # check if mem or instruction and calculate address
    #         if mem_idx == -1:
    #             address_local = 96 + (4 * inst_idx)
    #         else:
    #             address_local = 96 + (4 * Pipeline.num_instrs) + (4 * mem_idx)
    #
    #         # figure out which word in the block
    #         if address_local % 8 == 0:
    #             data_word = 0
    #             addr1 = address_local
    #             addr2 = address_local + 4
    #         elif address_local % 8 != 0:
    #             data_word = 1
    #             addr1 = address_local
    #             addr2 = address_local + 4
    #
    #         # if addr1 is instr, get instruction
    #         # else, get data
    #         if addr1 < 96 + (4 * Pipeline.num_instrs):
    #             data1 = Pipeline.instrs[Pipeline.get_mem_idx(addr1, True)]
    #         else:
    #             data1 = Pipeline.mem[Pipeline.get_mem_idx(addr1, False)]
    #
    #         # same thing for addr2
    #         if addr2 < 96 + (4 * Pipeline.num_instrs):
    #             data2 = Pipeline.instrs[Pipeline.get_mem_idx(addr2, True)]
    #         else:
    #             data2 = Pipeline.mem[Pipeline.get_mem_idx(addr2, False)]
    #
    #         if is_write and data_word == 0:
    #             data1 = data_to_write
    #         elif is_write and data_word == 1:
    #             data2 = data_to_write
    #
    #         # get set and tag for addr1
    #         set_num = (addr1 & Pipeline.set_msk) >> 3
    #         tag = (addr1 & Pipeline.tag_msk) >> 5
    #
    #         if Pipeline.sets[set_num][0][0] == 1 and Pipeline.sets[set_num][0][2] == tag:
    #             hit = True
    #             assoc_block = 0
    #         elif Pipeline.sets[set_num][1][0] == 1 and Pipeline.sets[set_num][1][2] == tag:
    #             hit = True
    #             assoc_block = 1
    #
    #         # if hit, update LRU and dirty bit if is_write = True
    #         if hit:
    #             if hit and is_write:
    #                 Pipeline.sets[set_num][assoc_block][1] = 1
    #                 Pipeline.lru[set_num] = (assoc_block + 1) % 2
    #                 Pipeline.sets[set_num][assoc_block][data_word + 3] = data_to_write
    #             Pipeline.lru[set_num] = (assoc_block + 1) % 2
    #             return [True, Pipeline.sets[set_num][assoc_block][data_word + 3]]
    #         else:  # miss
    #             # if we missed last time, take it out of the list and do the write
    #             if addr1 in Pipeline.missed_list:
    #                 while missed_list.count(addr1) > 0:
    #                     missed_list.remove(addr1)
    #                 # if dirty bit is 1 do write back
    #                 if sets[set_num][lru[set_num]][2] == 1:
    #                     wb_addr = sets[set_num][lru[set_num]][2]
    #                     wb_addr = (wb_addr << 5) + (set_num << 3)
    #                     if wb_addr >= (num_instrs * 4) + 96:
    #                         mem[get_mem_idx(wb_addr, False)] = sets[set_num][lru[set_num]][3]
    #                     if wb_addr + 4 >= (num_instrs * 4) + 96:
    #                         mem[get_mem_idx(wb_addr, False)] = sets[set_num][lru[set_num]][4]
    #
    #                 # write cache
    #
    #                 # valid = 1
    #                 sets[set_num][lru[set_num]][0] = 1
    #                 # dirty bit = 0 or 1 depending on is_write
    #                 sets[set_num][lru[set_num]][1] = 0
    #                 if is_write:
    #                     sets[set_num][lru[set_num]][1] = 1
    #                 # write tag, data1 and data2
    #                 sets[set_num][lru[set_num]][2] = tag
    #                 sets[set_num][lru[set_num]][3] = data1
    #                 sets[set_num][lru[set_num]][4] = data2
    #                 # change lru bit
    #                 lru[set_num] = (lru[set_num] + 1) % 2
    #
    #                 return [True, sets[set_num][(lru[set_num] + 1) % 2]][data_word + 3]
    #             else:
    #                 if missed_list.count(addr1) == 0:
    #                     missed_list.append(addr1)
    #                 return [False, 0]


    class Fetch:
        def __init__(self):
            pass

        @staticmethod
        def run(self):
            i = 0
            while pre_issue_buff[0] and pre_issue_buff[1] == -1:
                for i in range(len(self.instrs)):
                    # print self.opcodes
                    # self.opcodes = team12_Disassembler.opcode[i]
                    # self.dest = team12_Disassembler.arg3[i]
                    # self.src1 = team12_Disassembler.arg1[i]
                    # self.src2 = team12_Disassembler.arg2[i]
                    print self.instrs



                    opstr = team12_Disassembler.opcodeStr[i]
                    reg1 = team12_Disassembler.argStr1[i]
                    reg2 = team12_Disassembler.argStr2[i]
                    reg3 = team12_Disassembler.argStr3[i]

                    bitchin = self.dest + self.src1 + self.src2
                    # back_instr = str(self.opcodes) + " " + str(self.dest) + " " + str(self.src1) + " " + str(self.src2)
                    instr = opstr + " " + str(reg1) + " " + str(reg2) + " " + str(reg3)
                    if i ==2:
                        break
                    pre_issue_buff[i] = instr
                    print pre_issue_buff

                    # pre_issue_buff[0] = i + 1
                    # pre_issue_buff[i] = -1
                    print i

                # return pre_issue_buff[i]

                    # print pre_issue_buff
                    # print(team12_Disassembler.opcodeStr)





    class ALU:

        def __init__(self):
            pass

        @staticmethod
        def run(self):
            i = -1
            while pre_alu_buff[0] and pre_alu_buff[1] == -1:

                for i in range(len(team12_Disassembler.instructions)):
                    pre_alu_buff[0] = pre_issue_buff[0]
                    # print pre_alu_buff[0]
                    pre_alu_buff[1] = pre_issue_buff[1]

                    # print pre_alu_buff[1]
                    # pre_issue_buff[0] = " "
                    # pre_issue_buff[1] = " "
                    # if pre_alu_buff[0] == post_alu_buff[0]:
                    #     pre_alu_buff[0] = pre_alu_buff[1]

                    if post_alu_buff[0] == -1:
                        post_alu_buff[0] = pre_alu_buff[0]
                        pre_alu_buff[0] = pre_alu_buff[1]
                        pre_alu_buff[1] = -1

                        for k in range(len(team12_Disassembler.instructions)):
                            # print self.opcodes
                            self.opcodes = team12_Disassembler.opcode[i]
                            self.dest = team12_Disassembler.arg3[i]
                            self.src1 = team12_Disassembler.arg1[i]
                            self.src2 = team12_Disassembler.arg2[i]



                        print self.opcodes
                        print post_alu_buff
                        print self.dest
                        print self.src1
                        print self.src2


                        print "bitch2"

                        #not sure what variables will be yet but here is basic arithmetic
                        if self.opcodes == 1160:
                            print "cunt"
                            # print team12_Disassembler.dest[post_alu_buff[0]]
                            # print team12_Disassembler.src2[post_alu_buff[0]]
                            # print team12_Disassembler.src1[post_alu_buff[0]]
                            r[self.dest] = r[self.src1] + self.src2
                            self.opcodes = post_alu_buff.append(pre_alu_buff[0])

                        elif team12_Disassembler.opcodeStr == "B":
                            post_alu_buff[0] = post_alu_buff.append(pre_alu_buff[0])
                        elif self.opcodes == 1112:
                            print "cunt2"
                            r[self.dest] = self.src1 + self.src2
                            self.opcodes = post_alu_buff.append( pre_alu_buff[0])
                        elif team12_Disassembler.opcodeStr == "SUB":
                            r[self.dest[post_alu_buff[0]]] = self.src1[post_alu_buff[0]] - self.src2[post_alu_buff[0]]
                            post_alu_buff[0] = post_alu_buff.append( pre_alu_buff[0])
                        elif team12_Disassembler.opcodeStr == "SUBI":
                            r[self.dest[post_alu_buff[0]]] = self.src1[post_alu_buff[0]] - self.src2[post_alu_buff[0]]
                            post_alu_buff[0] = post_alu_buff.append( pre_alu_buff[0])
                        elif team12_Disassembler.opcodeStr == "AND":
                            r[self.dest[post_alu_buff[0]]] = self.src1[post_alu_buff[0]] & self.src2[post_alu_buff[0]]
                            post_alu_buff[0] = post_alu_buff.append( pre_alu_buff[0])
                        elif team12_Disassembler.opcodeStr == "ORR":
                            r[self.dest[post_alu_buff[0]]] = self.src1[post_alu_buff[0]] | self.src2[post_alu_buff[0]]
                            post_alu_buff[0] = post_alu_buff.append( pre_alu_buff[0])
                        elif team12_Disassembler.opcodeStr == "EOR":
                            r[self.dest[post_alu_buff[0]]] = self.src1[post_alu_buff[0]] ^ self.src2[post_alu_buff[0]]
                            post_alu_buff[0] = post_alu_buff.append( pre_alu_buff[0])
                        # elif team12_Disassembler.opcodeStr[post_alu_buff[0]] == "MOVZ":
                        #     p_num = pow(2,self.src1[post_alu_buff[0]])
                        #     r[self.dest[post_alu_buff[0]]] = p_num * self.src2[post_alu_buff[0]]
                        #     post_alu_buff[0] = post_alu_buff.append( pre_alu_buff[0])
                        # elif team12_Disassembler.opcodeStr[post_alu_buff[0]] == "MOVK":
                        #     p_num = pow(2, self.src1[post_alu_buff[0]])
                        #     r[self.dest[post_alu_buff[0]]] = p_num * self.src2[post_alu_buff[0]]
                        #     post_alu_buff[0] = post_alu_buff.append( pre_alu_buff[0] )
                        # elif team12_Disassembler.opcodeStr[post_alu_buff[0]] == "STUR":
                        #     post_alu_buff[0] = post_alu_buff.append( pre_alu_buff[0])
                        # elif team12_Disassembler.opcodeStr[post_alu_buff[0]] == "LDUR":
                        #     post_alu_buff[0] = post_alu_buff.append( pre_alu_buff[0])
                        # elif team12_Disassembler.opcodeStr[post_alu_buff[0]] == "CBZ":
                        #     if r[self.dest[post_alu_buff[0]]] == 0:
                        #         offset = self.src1[post_alu_buff[0]]
                        #         self.dest[post_alu_buff[0]] += offset - 1
                        #     post_alu_buff[0] = post_alu_buff.append( pre_alu_buff[0] )
                        # elif team12_Disassembler.opcodeStr[post_alu_buff[0]] == "CBNZ":
                        #     if r[self.dest[post_alu_buff[0]]] != 0:
                        #         offset = self.src1[post_alu_buff[0]]
                        #         self.dest[post_alu_buff[0]] += offset - 1
                        #     post_alu_buff[0] = post_alu_buff.append( pre_alu_buff[0] )
                        # elif team12_Disassembler.opcodeStr[post_alu_buff[0]] == "ASR":
                        #     r[self.dest[post_alu_buff[0]]] = self.src1[post_alu_buff[0]] / self.src2[post_alu_buff[0]]
                        #     post_alu_buff[0] = post_alu_buff.append(pre_alu_buff[0])
                        # elif team12_Disassembler.opcodeStr[post_alu_buff[0]] == "LSL":
                        #     p_num = pow(2, self.src2[post_alu_buff[0]])
                        #     r[self.dest[post_alu_buff[0]]] = p_num * self.src1[post_alu_buff[0]]
                        #     post_alu_buff[0] = post_alu_buff.append(pre_alu_buff[0])
                        # elif team12_Disassembler.opcodeStr[post_alu_buff[0]] == "LSR":
                        #     r[self.dest[post_alu_buff[0]]] = self.src1[post_alu_buff[0]] / self.src2[post_alu_buff[0]]
                        #     post_alu_buff[0] = post_alu_buff.append(pre_alu_buff[0])
                        # elif team12_Disassembler.opcodeStr[post_alu_buff[0]] == "NOP":
                        #     post_alu_buff[0] = post_alu_buff.append(pre_alu_buff[0])
                        # elif team12_Disassembler.opcodeStr[post_alu_buff[0]] == "BREAK":
                        #     post_alu_buff[0] = post_alu_buff.append(pre_alu_buff[0])
                        else:
                            print ("ERROR INSTRUCTION NOT RECOGNIZED")








if __name__ == "__main__":
    d = team12_Disassembler.TestMe()
    d.run()
    s = Pipeline( team12_Disassembler.instructions, team12_Disassembler.opcodeStr, team12_Disassembler.mem, team12_Disassembler.addrs,
                   team12_Disassembler.arg1,
                   team12_Disassembler.arg2, team12_Disassembler.arg3, team12_Disassembler.num_instrs, team12_Disassembler.dest, team12_Disassembler.src1,
                   team12_Disassembler.src2, 0 )
    s.run()



