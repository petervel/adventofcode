import math

DEBUG_LEVEL = 0
def debug(lvl, text):
    if lvl <= DEBUG_LEVEL:
        print(text)

class Amplifier:
    def __init__(self, data, input, output):
        self.data = data + ([0] * len(data))
        self.input = input
        self.output = output
        self.done = False
        self.step = 0
        self.base = 0

    def setInputs(self, input):
        self.input = input

    def setOutputs(self, outputs):
        self.outputs = outputs

    def run(self):
        while self.step < len(self.data):
            opcode = self.data[self.step]
            debug(2, "")
            debug(2, "step = " + str(self.step) + ", base = " + str(self.base) + ", data: " + str(self.data[self.step:]))
            debug(3,str(self.step) + ") " + str(opcode) + "input : " + str(self.input)+ ", output: " + str(self.output))

            modes = math.floor(opcode / 100)
            opcode = opcode % 100
            if opcode == 99:
                self.done = True
                break
            elif opcode == 1: # add
                self.add(modes)
            elif opcode == 2: # multiply
                self.multiply(modes)
            elif opcode == 3:  # input
                self.getInput(modes)
            elif opcode == 4:  # output
                self.giveOutput(modes)
            elif opcode == 5: # jnz
                self.jnz(modes)
            elif opcode == 6: # jz
                self.jz(modes)
            elif opcode == 7: # set flag if smaller
                self.isLess(modes)
            elif opcode == 8: # set flag if equal
                self.isEqual(modes)
            elif opcode == 9: # set base
                self.addBase(modes)
            else:
                print("UNKNOWN OPCODE " + str(opcode) + " at position " + str(self.step))
                exit(1)

    def add(self, modes): # opcode 1
        valA = self.getValue(modes, 1)
        valB = self.getValue(modes, 2)
        target = self.getAddress(modes, 3)
        debug(1,"data[" + str(target) + "] = " + str(valA) + " + " + str(valB))
        self.data[target] = valA + valB
        self.step += 4

    def multiply(self, modes): # opcode 2
        valA = self.getValue(modes, 1)
        valB = self.getValue(modes, 2)
        target = self.getAddress(modes, 3)
        debug(1,"data[" + str(target) + "] = " + str(valA) + " * " + str(valB))
        self.data[target] = valA * valB
        self.step += 4

    def getInput(self, modes): # opcode 3
        target = self.getAddress(modes, 1)
        #debug("storing value " + str(self.input) + " to location " + str(target))
        #self.data[target] = self.input.pop(0)
        val = int(input("Input:"))
        self.data[target] = val
        debug(2, "Setting data[" + str(target) + "] to " + str(val))
        self.step += 2

    def giveOutput(self, modes): # opcode 4
        valA = self.getValue(modes, 1)
        self.output.append(valA)
        self.step += 2

    def jnz(self, modes): # opcode 5
        valA = self.getValue(modes, 1)
        valB = self.getValue(modes, 2)
        debug(3, str(self.step) + ") modes " + str(modes) + ", instruction " + str(self.data[self.step]) + " , valA: " + str(valA) + ", valB " + str(valB))
        debug(2, "jumping to " + str(valB) + " if " + str(valA) + " != 0")
        if valA != 0:
            self.step = valB
            return
        self.step += 3

    def jz(self, modes): # opcode 6
        valA = self.getValue(modes, 1)
        valB = self.getValue(modes, 2)
        debug(2, "jumping to " + str(valB) + " if " + str(valA) + " == 0")
        if valA == 0:
            self.step = valB
            return
        self.step += 3

    def isLess(self, modes): # opcode 7
        valA = self.getValue(modes, 1)
        valB = self.getValue(modes, 2)
        target = self.getAddress(modes, 3)
        if valA < valB:
            debug(2, "data[" + str(target) + "] = 1 (because " + str(valA) + " < " + str(valB) + ")")
            self.data[target] = 1
        else:
            debug(2, "data[" + str(target) + "] = 0 (because " + str(valA) + " >= " + str(valB) + ")")
            self.data[target] = 0
        self.step += 4

    def isEqual(self, modes): # opcode 8
        valA = self.getValue(modes, 1)
        valB = self.getValue(modes, 2)
        target = self.getAddress(modes, 3)
        if valA == valB:
            self.data[target] = 1
        else:
            self.data[target] = 0
        debug(3,str(self.step) + ") modes " + str(modes) + ", instruction " + str(self.data[self.step]) + " , valA: " + str(valA) + ", valB " + str(valB) + ", target: " + str(target))
        self.step += 4

    def addBase(self, modes): # opcode 9
        valA = self.getValue(modes, 1)
        self.base += valA
        debug(1,"Base set to " + str(self.base) + " by adding " + str(valA))
        self.step += 2

    def getValue(self, modes, offset):
        for i in range(offset-1):
            modes = modes // 10
        mode = modes % 10

        if mode == 1:
            address = self.step + offset
            debug(2, "direct value " + str(self.data[address]))
        elif mode == 2:
            tmp = self.data[self.step + offset]
            address = self.base + tmp
            debug(2, "relative item at " + str(address) + " => " + str(self.data[address]))
        else:
            address = self.data[self.step + offset]
            debug(2, "memory item at " + str(address) + " => " + str(self.data[address]))

        val = self.data[address]
        debug(3,"getValue: " + str(self.step) + ", " + str(offset) + ", " + str(self.step + offset))
        #debug(2,"val at " + str(address) + " = " + str(val))
        return val

    def getAddress(self, modes, offset):
        for i in range(offset-1):
            modes = modes // 10
        mode = modes % 10
        address = None
        if mode == 1:
            print("Direct value address??!")
            exit(1)
        elif mode == 2:
            tmp = self.data[self.step + offset]
            address = self.base + tmp
            debug(2, "relative item at " + str(address) + " => " + str(self.data[address]))
        else:
            address = self.data[self.step + offset]
            debug(2, "memory item at " + str(address) + " => " + str(self.data[address]))
        return address

def main():
    output = []
    amp = Amplifier(data, [], output)
    amp.run()
    print("result: " + str(output))

test1 = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]
test2 = [1102,34915192,34915192,7,4,7,99,0]
test3 = [104,1125899906842624,99]

data = [1102,34463338,34463338,63,1007,63,34463338,63,1005,63,53,1102,3,1,1000,109,988,209,12,9,1000,209,6,209,3,203,0,1008,1000,1,63,1005,63,65,1008,1000,2,63,1005,63,904,1008,1000,0,63,1005,63,58,4,25,104,0,99,4,0,104,0,99,4,17,104,0,99,0,0,1102,1,30,1010,1102,1,38,1008,1102,1,0,1020,1102,22,1,1007,1102,26,1,1015,1102,31,1,1013,1102,1,27,1014,1101,0,23,1012,1101,0,37,1006,1102,735,1,1028,1102,1,24,1009,1102,1,28,1019,1102,20,1,1017,1101,34,0,1001,1101,259,0,1026,1101,0,33,1018,1102,1,901,1024,1101,21,0,1016,1101,36,0,1011,1102,730,1,1029,1101,1,0,1021,1102,1,509,1022,1102,39,1,1005,1101,35,0,1000,1102,1,506,1023,1101,0,892,1025,1101,256,0,1027,1101,25,0,1002,1102,1,29,1004,1102,32,1,1003,109,9,1202,-3,1,63,1008,63,39,63,1005,63,205,1001,64,1,64,1106,0,207,4,187,1002,64,2,64,109,-2,1208,-4,35,63,1005,63,227,1001,64,1,64,1105,1,229,4,213,1002,64,2,64,109,5,1206,8,243,4,235,1106,0,247,1001,64,1,64,1002,64,2,64,109,14,2106,0,1,1105,1,265,4,253,1001,64,1,64,1002,64,2,64,109,-25,1201,4,0,63,1008,63,40,63,1005,63,285,1106,0,291,4,271,1001,64,1,64,1002,64,2,64,109,14,2107,37,-7,63,1005,63,313,4,297,1001,64,1,64,1106,0,313,1002,64,2,64,109,-7,21101,40,0,5,1008,1013,37,63,1005,63,333,1105,1,339,4,319,1001,64,1,64,1002,64,2,64,109,-7,1207,0,33,63,1005,63,355,1106,0,361,4,345,1001,64,1,64,1002,64,2,64,109,7,21102,41,1,9,1008,1017,41,63,1005,63,387,4,367,1001,64,1,64,1106,0,387,1002,64,2,64,109,-1,21102,42,1,10,1008,1017,43,63,1005,63,411,1001,64,1,64,1106,0,413,4,393,1002,64,2,64,109,-5,21101,43,0,8,1008,1010,43,63,1005,63,435,4,419,1106,0,439,1001,64,1,64,1002,64,2,64,109,16,1206,3,455,1001,64,1,64,1106,0,457,4,445,1002,64,2,64,109,-8,21107,44,45,7,1005,1017,479,4,463,1001,64,1,64,1106,0,479,1002,64,2,64,109,6,1205,5,497,4,485,1001,64,1,64,1106,0,497,1002,64,2,64,109,1,2105,1,6,1105,1,515,4,503,1001,64,1,64,1002,64,2,64,109,-10,2108,36,-1,63,1005,63,535,1001,64,1,64,1105,1,537,4,521,1002,64,2,64,109,-12,2101,0,6,63,1008,63,32,63,1005,63,561,1001,64,1,64,1105,1,563,4,543,1002,64,2,64,109,25,21108,45,46,-2,1005,1018,583,1001,64,1,64,1105,1,585,4,569,1002,64,2,64,109,-23,2108,34,4,63,1005,63,607,4,591,1001,64,1,64,1106,0,607,1002,64,2,64,109,3,1202,7,1,63,1008,63,22,63,1005,63,633,4,613,1001,64,1,64,1106,0,633,1002,64,2,64,109,12,21108,46,46,3,1005,1015,651,4,639,1106,0,655,1001,64,1,64,1002,64,2,64,109,-5,2102,1,-1,63,1008,63,35,63,1005,63,679,1001,64,1,64,1105,1,681,4,661,1002,64,2,64,109,13,21107,47,46,-7,1005,1013,701,1001,64,1,64,1105,1,703,4,687,1002,64,2,64,109,-2,1205,2,715,1106,0,721,4,709,1001,64,1,64,1002,64,2,64,109,17,2106,0,-7,4,727,1105,1,739,1001,64,1,64,1002,64,2,64,109,-23,2107,38,-6,63,1005,63,759,1001,64,1,64,1106,0,761,4,745,1002,64,2,64,109,-3,1207,-4,40,63,1005,63,779,4,767,1105,1,783,1001,64,1,64,1002,64,2,64,109,-8,2101,0,-1,63,1008,63,35,63,1005,63,809,4,789,1001,64,1,64,1105,1,809,1002,64,2,64,109,-6,2102,1,8,63,1008,63,32,63,1005,63,835,4,815,1001,64,1,64,1106,0,835,1002,64,2,64,109,6,1201,5,0,63,1008,63,37,63,1005,63,857,4,841,1106,0,861,1001,64,1,64,1002,64,2,64,109,2,1208,0,32,63,1005,63,883,4,867,1001,64,1,64,1106,0,883,1002,64,2,64,109,23,2105,1,-2,4,889,1001,64,1,64,1106,0,901,4,64,99,21102,27,1,1,21101,0,915,0,1106,0,922,21201,1,55337,1,204,1,99,109,3,1207,-2,3,63,1005,63,964,21201,-2,-1,1,21101,0,942,0,1105,1,922,21202,1,1,-1,21201,-2,-3,1,21102,957,1,0,1105,1,922,22201,1,-1,-2,1106,0,968,21201,-2,0,-2,109,-3,2105,1,0]

main()