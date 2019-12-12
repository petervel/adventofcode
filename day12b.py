class Moon:
    def __init__(self, coords):
        self.pos = coords.copy()
        self.vel = [0] * 3

    def updateSpeed(self, other):
        for i in range(3):
            if self.pos[i] < other.pos[i]:
                self.vel[i] += 1
            elif self.pos[i] > other.pos[i]:
                self.vel[i] -= 1

    def updatePosition(self):
        for i in range(3):
            self.pos[i] += self.vel[i]

    def print(self):
        print("pos=<x=" + str(self.pos[0]) + ", y=  " + str(self.pos[1]) + ", z= " + str(self.pos[2]) + ">, vel=<x=" + str(self.vel[0]) + ", y=  " + str(self.vel[1]) + ", z= " + str(self.vel[2]) + ">")

    def getPotential(self):
        sum = 0
        for i in range(3):
            sum += abs(self.pos[i])
        return sum

    def getKinetic(self):
        sum = 0
        for i in range(3):
            sum += abs(self.vel[i])
        return sum

    def getTotalEnergy(self):
        return self.getPotential() * self.getKinetic()

    def toShortString(self, dimension):
        return str(self.pos[dimension]) + "," + str(self.vel[dimension])

class Universe:
    def __init__(self, data):
        self.history = {}
        self.moons = []
        for d in data:
            self.moons.append(Moon(d))

    def log(self, dimension):
        curNode = self.history
        for i in range(len(self.moons)):
            hash = self.moons[i].toShortString(dimension)
            if hash not in curNode:
                curNode[hash] = {}
            elif i == (len(self.moons) - 1):
                return True
            curNode = curNode[hash]
        return False

    def updatePositions(self):
        for moon in self.moons:
            moon.updatePosition()

    def print(self):
        for moon in self.moons:
            moon.print()

    def tick(self):
        for i, moon in enumerate(self.moons):
            for j, moon2 in enumerate(self.moons):
                if i == j:
                    continue
                moon.updateSpeed(moon2)
        self.updatePositions()

def gcd(x, y):
   while(y):
       x, y = y, x % y
   return x

def lcm(x, y):
   lcm = (x*y)//gcd(x,y)
   return lcm

# x loops after 231614
# y loops after 116328
# z loops after 102356
def main():
    results = []

    # each dimension (x,y,z)
    for dimension in range(3):
        universe = Universe(input)

        step = 0
        while True:
            if universe.log(dimension):
                break

            universe.tick()
            step += 1

        results.append(step)
        print("stopping for dimension " + str(dimension) + " after " + str(step))

    loop = lcm(results[0], lcm(results[1], results[2]))
    print("universe loops after " + str(loop))

input = [
    [6, 10, 10],
    [-9, 3, 17],
    [9, -4, 14],
    [4, 14, 4],
]

test1 = [
    [-1, 0, 2],
    [2, -10, -7],
    [4, -8, 8],
    [3, 5, -1],
]

test2 = [
    [-8,-10,0],
    [5,5,10],
    [2,-7,3],
    [9,-8,-3],
]

main()