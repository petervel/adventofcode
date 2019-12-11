import math

DEBUG_LEVEL = 0
def debug(lvl, text):
    if lvl <= DEBUG_LEVEL:
        print(text)

class Processor:
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
            self.runStep()

    def runStep(self, wantOutput = False):
        opcode = self.data[self.step]
        debug(2, "step = " + str(self.step) + ", base = " + str(self.base) + ", data: " + str(self.data[self.step:]))
        debug(2, str(self.step) + ") opcode: " + str(opcode) + ", input : " + str(self.input)+ ", output: " + str(self.output))

        modes = math.floor(opcode / 100)
        opcode = opcode % 100
        if opcode == 99:
            self.done = True
            print("DONE!")
            return
        elif opcode == 1: # add
            self.add(modes)
        elif opcode == 2: # multiply
            self.multiply(modes)
        elif opcode == 3:  # input
            if len(self.input) == 0:
                # not ready for this, do not update step
                return
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

        if wantOutput and len(self.output) < 2:
            self.runStep(wantOutput)

    def add(self, modes): # opcode 1
        valA = self.getValue(modes, 1)
        valB = self.getValue(modes, 2)
        target = self.getAddress(modes, 3)
        debug(2,"data[" + str(target) + "] = " + str(valA) + " + " + str(valB))
        self.data[target] = valA + valB
        self.step += 4

    def multiply(self, modes): # opcode 2
        valA = self.getValue(modes, 1)
        valB = self.getValue(modes, 2)
        target = self.getAddress(modes, 3)
        debug(2,"data[" + str(target) + "] = " + str(valA) + " * " + str(valB))
        self.data[target] = valA * valB
        self.step += 4

    def getInput(self, modes): # opcode 3
        target = self.getAddress(modes, 1)
        #debug("storing value " + str(self.input) + " to location " + str(target))
        #val = int(input("Input:"))
        val = self.input.pop(0)
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
        else:
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
        debug(2,"Base set to " + str(self.base) + " by adding " + str(valA))
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

DIRECTIONS = [
    [0, -1],
    [1, 0],
    [0, 1],
    [-1, 0],
]

class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.data = []
        for y in range(height):
            row = []
            for x in range(width):
                row.append('.')
            self.data.append(row)

    def setAt(self, x, y, val):
        self.data[y][x] = val

    def getAt(self, x, y):
        return self.data[y][x]

    def print(self):
        for y, row in enumerate(self.data):
            rowStr = ""
            for x, c in enumerate(row):
                if c == '.':
                    rowStr += '█'
                else:
                    rowStr += c
            print(rowStr)

    def countNot(self, c):
        counter = 0
        for y, row in enumerate(self.data):
            for x, d in enumerate(row):
                if d != c:
                    counter += 1
        return counter

class Robot:
    def __init__(self, software):
        self.readings = []
        self.commands = []
        self.brain = Processor(software, self.readings, self.commands)

        width = 43
        height = 6
        self.pos = [int(0), int(0)]
        self.direction = 0

        self.grid = Grid(width, height)

        self.updateSensors()

    def move(self):
        self.pos[0] += DIRECTIONS[self.direction][0]
        self.pos[1] += DIRECTIONS[self.direction][1]

    def turnLeft(self):
        self.direction = (self.direction + len(DIRECTIONS) - 1) % len(DIRECTIONS)

    def turnRight(self):
        self.direction = (self.direction + len(DIRECTIONS) + 1) % len(DIRECTIONS)

    def rotate(self, direction):
        if direction == 0:
            self.turnLeft()
        else:
            self.turnRight()
        self.move()

    def paint(self, color):
        if color == 0:
            self.grid.setAt(self.pos[0], self.pos[1], ' ')
        elif color == 1:
            self.grid.setAt(self.pos[0], self.pos[1], '█')

    def processCommand(self, color, rotation):
        self.paint(color)
        self.rotate(rotation)
        self.updateSensors()
        debug(1, "Got rotate " + str(rotation) + ", moved robot: (" + str(self.pos))

    def updateSensors(self):
        color = self.grid.getAt(self.pos[0], self.pos[1])
        val = 1
        if color == ' ':
            val = 0
        elif color == '█':
            val = 1
        self.readings.append(val)

    def run(self):
        while True:
            self.brain.runStep(True)
            if self.brain.done:
                self.grid.print()
                cnt = self.grid.countNot('.')
                print("Total painted: " + str(cnt))
                break

            color = self.brain.output.pop(0)
            rotation = self.brain.output.pop(0)
            self.processCommand(color, rotation)

def main():
    robot = Robot(data)
    result = robot.run()
    print("result: " + str(result))

data = [
    3,8,1005,8,328,1106,0,11,0,0,0,104,1,104,0,3,8,1002,8,-1,10,1001,10,1,10,4,10,1008,8,0,10,4,10,1001,8,0,29,1,104,7,10,3,8,1002,8,-1,10,101,1,10,10,4,10,1008,8,0,10,4,10,1001,8,0,55,1,2,7,10,1006,0,23,3,8,102,-1,8,10,1001,10,1,10,4,10,1008,8,0,10,4,10,1001,8,0,84,1006,0,40,1,1103,14,10,1,1006,16,10,3,8,102,-1,8,10,101,1,10,10,4,10,108,1,8,10,4,10,1002,8,1,116,1006,0,53,1,1104,16,10,3,8,102,-1,8,10,101,1,10,10,4,10,1008,8,1,10,4,10,102,1,8,146,2,1104,9,10,3,8,102,-1,8,10,101,1,10,10,4,10,1008,8,1,10,4,10,1001,8,0,172,1006,0,65,1,1005,8,10,1,1002,16,10,3,8,102,-1,8,10,1001,10,1,10,4,10,108,0,8,10,4,10,102,1,8,204,2,1104,9,10,1006,0,30,3,8,102,-1,8,10,101,1,10,10,4,10,108,0,8,10,4,10,102,1,8,233,2,1109,6,10,1006,0,17,1,2,6,10,3,8,102,-1,8,10,101,1,10,10,4,10,108,1,8,10,4,10,102,1,8,266,1,106,7,10,2,109,2,10,2,9,8,10,3,8,102,-1,8,10,101,1,10,10,4,10,1008,8,1,10,4,10,1001,8,0,301,1,109,9,10,1006,0,14,101,1,9,9,1007,9,1083,10,1005,10,15,99,109,650,104,0,104,1,21102,1,837548789788,1,21101,0,345,0,1106,0,449,21101,0,846801511180,1,21101,0,356,0,1106,0,449,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,21101,235244981271,0,1,21101,403,0,0,1105,1,449,21102,1,206182744295,1,21101,0,414,0,1105,1,449,3,10,104,0,104,0,3,10,104,0,104,0,21102,837896937832,1,1,21101,0,437,0,1106,0,449,21101,867965862668,0,1,21102,448,1,0,1106,0,449,99,109,2,22102,1,-1,1,21101,40,0,2,21102,1,480,3,21101,0,470,0,1106,0,513,109,-2,2106,0,0,0,1,0,0,1,109,2,3,10,204,-1,1001,475,476,491,4,0,1001,475,1,475,108,4,475,10,1006,10,507,1101,0,0,475,109,-2,2106,0,0,0,109,4,1201,-1,0,512,1207,-3,0,10,1006,10,530,21102,1,0,-3,22102,1,-3,1,21201,-2,0,2,21102,1,1,3,21102,549,1,0,1106,0,554,109,-4,2105,1,0,109,5,1207,-3,1,10,1006,10,577,2207,-4,-2,10,1006,10,577,21202,-4,1,-4,1106,0,645,21202,-4,1,1,21201,-3,-1,2,21202,-2,2,3,21101,596,0,0,1106,0,554,21201,1,0,-4,21102,1,1,-1,2207,-4,-2,10,1006,10,615,21101,0,0,-1,22202,-2,-1,-2,2107,0,-3,10,1006,10,637,22102,1,-1,1,21101,637,0,0,105,1,512,21202,-2,-1,-2,22201,-4,-2,-4,109,-5,2106,0,0
]

main()