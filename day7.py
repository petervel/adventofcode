import math
import itertools

dataInput = [3,8,1001,8,10,8,105,1,0,0,21,34,47,72,81,94,175,256,337,418,99999,3,9,102,3,9,9,1001,9,3,9,4,9,99,3,9,101,4,9,9,1002,9,5,9,4,9,99,3,9,1001,9,5,9,1002,9,5,9,1001,9,2,9,1002,9,5,9,101,5,9,9,4,9,99,3,9,102,2,9,9,4,9,99,3,9,1001,9,4,9,102,4,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,99]
testData = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
testData2= [3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0]

testB1 = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
testB2 = [3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10]

DEBUG_MODE = False
def debug(text):
    if DEBUG_MODE:
        print(text)

class Amplifier:
    def __init__(self, data, input, output):
        self.data = data
        self.input = input
        self.output = output
        self.done = False
        self.step = 0

    def setInputs(self, input):
        self.input = input

    def setOutputs(self, outputs):
        self.outputs = outputs

    def run(self):
        while self.step < len(self.data):
            opcode = self.data[self.step]

            debug(self.data)
            debug(self.input)
            debug(str(self.step) + ") " + str(opcode))

            modes = math.floor(opcode / 100)
            opcode = opcode % 100
            if opcode == 99:
                self.done = True
                break
            elif opcode == 1: # add
                self.step += self.opcode1(modes)
            elif opcode == 2: # multiply
                self.step += self.opcode2(modes)
            elif opcode == 3:  # input
                if len(self.input) == 0:
                    print("no input. stopping")
                    return # stop for now
                self.step += self.opcode3(modes)
            elif opcode == 4:  # output
                self.step += self.opcode4(modes)
                return # after 1 output, the next one should run first
            elif opcode == 5: # jnz
                self.step = self.opcode5(modes)
            elif opcode == 6: # jz
                self.step = self.opcode6(modes)
            elif opcode == 7: # set flag if smaller
                self.step += self.opcode7(modes)
            elif opcode == 8: # set flag if equal
                self.step += self.opcode8(modes)
            else:
                print("UNKNOWN OPCODE " + str(opcode) + " at position " + str(self.step))
                exit(1)

    def getValue(self, modes, offset):
        for i in range(offset-1):
            modes = modes // 10
        mode = modes % 10

        if mode == 1:
            address = self.step + offset
        else:
            address = self.data[self.step + offset]

        val = self.data[address]
        debug(str(self.step) + ", " + str(offset) + ", " + str(self.step + offset))
        debug("val at " + str(address) + " = " + str(val))
        return val

    def opcode1(self, modes):
        valA = self.getValue(modes, 1)
        valB = self.getValue(modes, 2)
        target = self.data[self.step + 3]
        self.data[target] = valA + valB
        debug(str(self.step) + ") modes " + str(modes) + ", instruction " + str(self.data[self.step]) + " , valA: " + str(valA) + ", valB " + str(valB) + ", target: " + str(target))
        return 4

    def opcode2(self, modes):
        valA = self.getValue(modes, 1)
        valB = self.getValue(modes, 2)
        target = self.data[self.step + 3]
        self.data[target] = valA * valB
        debug(str(self.step) + ") modes " + str(modes) + ", instruction " + str(self.data[self.step]) + " , valA: " + str(valA) + ", valB " + str(valB) + ", target: " + str(target))
        return 4

    def opcode3(self, modes):
        target = self.data[self.step + 1]
        debug("storing value " + str(self.input) + " to location " + str(target))
        self.data[target] = self.input.pop(0)
        return 2

    def opcode4(self, modes):
        valA = self.getValue(modes, 1)
        self.output.append(valA)
        return 2

    def opcode5(self, modes):
        valA = self.getValue(modes, 1)
        valB = self.getValue(modes, 2)
        debug(str(self.step) + ") modes " + str(modes) + ", instruction " + str(self.data[self.step]) + " , valA: " + str(valA) + ", valB " + str(valB))
        if valA != 0:
            return valB
        return self.step + 3

    def opcode6(self, modes):
        valA = self.getValue(modes, 1)
        valB = self.getValue(modes, 2)
        if valA == 0:
            return valB
        return self.step + 3

    def opcode7(self, modes):
        valA = self.getValue(modes, 1)
        valB = self.getValue(modes, 2)
        target = self.data[self.step + 3]
        if valA < valB:
            self.data[target] = 1
        else:
            self.data[target] = 0
        return 4

    def opcode8(self, modes):
        valA = self.getValue(modes, 1)
        valB = self.getValue(modes, 2)
        target = self.data[self.step + 3]
        if valA == valB:
            self.data[target] = 1
        else:
            self.data[target] = 0
        debug(str(self.step) + ") modes " + str(modes) + ", instruction " + str(self.data[self.step]) + " , valA: " + str(valA) + ", valB " + str(valB) + ", target: " + str(target))
        return 4

def bruteInstance(data, params):
    amps = []
    input = [params[0], 0]
    firstInput = input
    for i in range(5):
        if i != 4:
            output = [params[i + 1]]
        else:
            output = firstInput
        amps.append(Amplifier(data.copy(), input, output))
        input = output

    i = 0
    done = {}
    while True:
        amp = amps[i]
        debug("running amp " + str(i) + ")" + ", inp: " + str(amp.input) + ", out: " + str(amp.output))
        amp.run()
        if amp.done:
            debug(str(i) + " is done!")
            done[i] = True
            if len(done) == 5:
                return amp.output[0]
        i =  (i + 1) % 5

def brute(data, values):
    best = 0
    bestParams = []
    for params in itertools.permutations(values):
        result = bruteInstance(data, params)
        print(str(params) + " ==> " + str(result))
        if result != None and result > best:
            bestParams = params
            best = result
    return [best, bestParams]

def main():
    val = brute(dataInput, range(5,10))
    print("result: " + str(val[0]) + " (" + str(val[1]) + ")")

main()