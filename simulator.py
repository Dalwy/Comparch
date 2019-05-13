import disassembler
import sys


pre_issue_buff = [-1, -1, -1, -1]
pre_alu_buff = [-1, -1]
pre_mem_buff = [-1, -1]
post_mem_buff = [-1, -1]
post_alu_buff = [-1, -1]
r = [0] * 32
data = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]
data_start = disassembler.Memory
data_rows = [data_start, data_start + 32, data_start + 64, data_start + 96]

sets = [[[0,0,0,0,0],[0,0,0,0,0]], [[0,0,0,0,0],[0,0,0,0,0]],
        [[0,0,0,0,0],[0,0,0,0,0]], [[0,0,0,0,0],[0,0,0,0,0]]]
            
lru = [0,0,0,0]
tag_msk = 4294967264
set_msk = 24
missed_list = []

class Simulator:


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
        output_file.write("Cycle: " + str(self.cycle) + "\n")
        output_file.write("Pre-Issue Buffer:" + "\n")
        for i in range(len(pre_issue_buff)):
            output_file.write("Entry " + str(i) + ":" + str(pre_issue_buff[i]) + "\n")
        output_file.write("Pre_ALU Queue:" + "\n")
        for i in range(len(pre_alu_buff)):
            output_file.write("Entry " + str(i) + ":" + str(pre_alu_buff[i]) + "\n")
        output_file.write("Post_ALU Queue:" + "\n")
        for i in range(len(post_alu_buff)):
            output_file.write("Entry " + str(i) + ":" + str(post_alu_buff[i]) + "\n")
        output_file.write("Pre_MEM Queue:" + "\n")
        for i in range(len(pre_mem_buff)):
            output_file.write("Entry " + str(i) + ":" + str(pre_mem_buff[i]) + "\n")
        output_file.write("Post_MEM Queue:" + "\n")
        for i in range(len(post_mem_buff)):
            output_file.write("Entry " + str(i) + ":" + str(post_mem_buff[i]) + "\n")
        output_file.write("Registers:" + "\n")
        output_file.write("R00:" + "\t")
        for i in range(len(r)):
            if i == 8 or i == 16 or i == 24:
                output_file.write("\n")
                if i == 8:
                    output_file.write("R0" + str(i) + "\t")
                else:
                    output_file.write("R" + str(i) + "\t")
            output_file.write(str(r[i]) + "\t")
    
    def print_data(self, output_file):
        for data_list in data:
                    for addi in data_list:
                        if addi != 0:
                            for row, address in zip(data_rows, data):
                                output_file.write(str(row) + ': ')
                                for add in address:
                                    output_file.write(str(add) + '\t')
                                output_file.write('\n')
                        else:
                            continue

    def get_mem_idx(self, address, is_instr):
        if is_instr is False:
            return (address - (96 + (self.num_instrs * 4))) / 4
        else:
            return (address - 96) / 4
    
    def is_mem_op(self, index):
        if self.opcodes[index] == "STUR" or self.opcodes[index] == "LDUR":
            return True
        else:
            return False

    def run(self):

        for i in range(len(sys.argv)):
            if sys.argv[i] == '-i' and i < (len(sys.argv) - 1):
                input_file = sys.argv[i + i]
            elif sys.argv[i] == '-o' and i < (len(sys.argv) - 1):
                output_file = sys.argv[i + 1]
        
        output_file = open(output_file + "_sim.txt", 'w')
        Issue = self.get_issue()
        Fetch = self.get_fetch()
        Cache = self.get_cache()
        booyakasha = True
        while booyakasha:
            self.WB.run()
            self.MEM.run()
            Issue.run()
            booyakasha = Fetch.run()
            self.print_state(output_file)
            self.cycle += 1
    
    class WB:

        def __init__(self):
            pass

        @staticmethod
        def run():

            if post_alu_buff[1] != -1:
                r[post_alu_buff[1]] = post_alu_buff[0]
                post_alu_buff[0] = -1
                post_alu_buff[1] = -1
            if post_mem_buff[1] != -1:
                r[post_mem_buff[1]] = post_mem_buff[0]
                post_mem_buff[0] = -1
                post_mem_buff[1] = -1
            

    class MEM:

        def __init__(self):
            pass
        
        @staticmethod
        def run():
            # check to see if first pos is empty
            if pre_mem_buff[0] != -1:
                i = pre_mem_buff[0]  # set index to work with
                if opcodes[i] == "STUR":
                    isSW = True
                    hit_data = Simulator.Cache.access_mem(-1, i, isSW, r[src2[i]])
                    if hit_data[0] is True:
                        pre_mem_buff[0] = pre_mem_buff[1]
                        pre_mem_buff[1] = -1
                else:
                    isSW = False
                    hit_data = Simulator.Cache.access_mem(-1, i, isSW, r[src2[i]])
                    if hit_data[0] is True:
                        post_mem_buff[0] = hit_data[1]
                        pre_mem_buff[0] = pre_mem_buff[1]
                        pre_mem_buff[1] = -1
    
    def get_issue(self):
        class Issue:
            @staticmethod
            def run():
                # find number in buff
                num_in_buff = 0
                num_issued = 0
                curr = 0
                issue_me = True

                for idx in pre_issue_buff:
                    if idx != -1:
                        num_in_buff += 1
                
                while num_issued < 2 and num_in_buff > 0:
                    if curr < 4:
                        index = pre_issue_buff[curr]
                    if self.is_mem_op(index):
                        for i in range(0, len(pre_mem_buff)):
                            if pre_alu_buff[i] != -1:
                                if self.dest[index] == self.src1[pre_mem_buff[i]] or self.dest[index] == self.src2[pre_mem_buff[i]]:
                                    issue_me = False
                                    break
                    elif not self.is_mem_op(index):
                        for i in range(0, len(pre_alu_buff)):
                            if pre_alu_buff[i] != -1:
                                if self.dest[index] == self.src1[pre_alu_buff[i]] or self.dest[index] == self.src2[pre_alu_buff[i]]:
                                    issue_me = False
                                    break
                    
                    if issue_me:
                        num_issued += 1

                        if self.is_mem_op(index):
                            pre_mem_buff[pre_mem_buff.index(-1)] = index
                        else:
                            print(pre_alu_buff)
                            pre_alu_buff[pre_alu_buff.index(-1)] = index
                        
                        pre_issue_buff.pop(0)
                        pre_issue_buff.append(-1)
                        num_in_buff -= 1
                        curr += 1
        return Issue()

    def get_fetch(self):

        class Fetch():
            @staticmethod        
            def run():
                Cache = self.get_cache()
                num_fetched = 0
                while num_fetched != 2:
                    if -1 not in pre_issue_buff:
                        return True
                    if self.opcodes[self.cycle] == "BREAK":
                        return False
                    hit_data = Cache.access_mem(-1, self.cycle, self.is_mem_op(self.cycle))
                    if hit_data[0] == True and pre_issue_buff.count(-1) > 0:
                        pre_issue_buff[pre_issue_buff.index(-1)] = hit_data[1]
                        num_fetched += 1
                        return True
                    if hit_data[0] == False:
                        return True
                return True
        
        return Fetch()

                
    def get_cache(self):
        class Cache:
            
            @staticmethod
            def flush():
                print("Flush, bitch")

            @staticmethod
            def access_mem(mem_idx, inst_idx, is_write, data_to_write=0):
                # check if mem or instruction and calculate address
                hit = True
                assoc_block = 0

                if mem_idx == -1:
                    address_local = 96 + (4 * inst_idx)
                else:
                    address_local = 96 + (4 * self.num_instrs) + (4 * mem_idx)
                # figure out which word in the block
                if address_local % 8 == 0:
                    data_word = 0
                    addr1 = address_local
                    addr2 = address_local + 4
                elif address_local % 8 != 0:
                    data_word = 1
                    addr1 = address_local
                    addr2 = address_local + 4

                # if addr1 is instr, get instruction
                # else, get data
                if addr1 < 96 + (4 * self.num_instrs):
                    data1 = self.instrs[self.get_mem_idx(addr1, True)]
                else:
                    data1 = self.mem[self.get_mem_idx(addr1, False)]

                # same thing for addr2
                if addr2 < 96 + (4 * self.num_instrs):
                    data2 = self.instrs[self.get_mem_idx(addr2, True)]
                else:
                    data2 = self.mem[self.get_mem_idx(addr2, False)]
                
                # get set and tag for addr1
                set_num = (addr1 & set_msk) >> 3
                tag = (addr1 & tag_msk) >> 5
                if sets[set_num][0][0] == 1 and sets[set_num][0][2] == tag:
                    hit = True
                    assoc_block = 0
                elif sets[set_num][1][0] == 1 and sets[set_num][1][2] == tag:
                    hit = True
                    assoc_block = 1
                # if hit, update LRU and dirty bit if is_write = True
                if hit:
                    if hit and is_write:
                        sets[set_num][assoc_block][1] = 1
                        lru[set_num] = (assoc_block + 1) % 2
                        sets[set_num][assoc_block][data_word + 3] = data_to_write
                    lru[set_num] = (assoc_block + 1) % 2
                    return [True, sets[set_num][assoc_block][data_word + 3]]
                else:  # miss
                    # if we missed last time, take it out of the list and do the write
                    if addr1 in missed_list:
                        while missed_list.count(addr1) > 0:
                            missed_list.remove(addr1)
                        # if dirty bit is 1 do write back    
                        if sets[set_num][lru[set_num]][2] == 1:
                            wb_addr = sets[set_num][lru[set_num]][2]
                            wb_addr = (wb_addr << 5) + (set_num << 3)
                            if wb_addr >= (self.num_instrs * 4) + 96:
                                self.mem[self.get_mem_idx(wb_addr, False)] = sets[set_num][lru[set_num]][3]
                            if wb_addr + 4 >= (self.num_instrs * 4) + 96:
                                self.mem[self.get_mem_idx(wb_addr, False)] = sets[set_num][lru[set_num]][4]

                        # write cache

                        # valid = 1
                        sets[set_num][lru[set_num]][0] = 1
                        # dirty bit = 0 or 1 depending on is_write
                        sets[set_num][lru[set_num]][1] = 0
                        if is_write:
                            sets[set_num][lru[set_num]][1] = 1
                        # write tag, data1 and data2
                        sets[set_num][lru[set_num]][2] = tag
                        sets[set_num][lru[set_num]][3] = data1
                        sets[set_num][lru[set_num]][4] = data2
                        # change lru bit
                        lru[set_num] = (lru[set_num] + 1) % 2

                        return [True, sets[set_num][(lru[set_num] + 1) % 2]][data_word + 3]
                    else:
                        if missed_list.count(addr1) == 0:
                            missed_list.append(addr1)
                        return [False, 0]
        return Cache()




            


if __name__ == "__main__":
    d = disassembler.Disassembler()
    d.run()
    s = Simulator(disassembler.instructions, disassembler.opcodeStr, disassembler.mem, disassembler.addrs, disassembler.arg1,
                  disassembler.arg2, disassembler.arg3, len(disassembler.instructions), disassembler.dest, disassembler.src1, 
                  disassembler.src2, 0)
    s.run()    
        
    


