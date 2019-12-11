import math

def pad(s):
    while len(s) < 4:
        s = " " + s
    return s

BASE_X = 20
BASE_Y = 19

class Asteroid:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getAngle(self):
        fromX = BASE_X
        fromY = BASE_Y  # cheating a bit cos I'm lazy
        relX = self.x - fromX
        relY = fromY - self.y
        rads = math.atan2(relX, relY)
        degs = math.degrees(rads)
        if degs < 0:
            degs += 360
        #print(str(self.x) + "," + str(self.y) + " ==> " +str(relX) + "," + str(relY) + "," + str(degs))
        return degs

    def getDistance(self):
        fromX = BASE_X
        fromY = BASE_Y # cheating a bit cos I'm lazy
        x2 = (self.x - fromX)**2
        y2 = (self.y - fromY)**2
        return math.sqrt(x2 + y2)

    def printCoordinates(self):
        print("(" + str(self.x) + "," + str(self.y) + ")")

    def printDetails(self):
        print("(" + str(self.x) + "," + str(self.y) + ") => angle=" + str(self.getAngle()) + ", dist=" + str(self.getDistance()))

    def boom(self, counter):
        ext = "th"
        if counter == 1:
            ext = "st"
        elif counter == 2:
            ext = "nd"
        elif counter == 3:
            ext = "rd"
        #self.printDetails()
        print("The " + str(counter) + ext + " asteroid to be vaporized is at " + str(self.x) + "," + str(self.y) + ".")

def createData(grid):
    data = []
    for y, row in enumerate(grid):
        for x, c in enumerate(row):
            if x == BASE_X and y == BASE_Y:
                continue
            if c == '#':
                data.append(Asteroid(x, y))

    return sorted(data, key = lambda x: (x.getAngle(), x.getDistance()))

def groupByAngle(data):
    result = {}
    for ast in data:
        k = str(math.floor(ast.getAngle()*1000000))
        if k not in result:
            result[k] = []
        #ast.printCoordinates()
        result[k].append(ast)
    return result

def shootEm(data):
    counter = 1
    while len(data) > 0:
        for k in list(data.keys()):
            ar = data[k]

            ast = data[k].pop(0)
            if len(ar) == 0:
                del data[k]

            ast.boom(counter)
            counter += 1

def resolve(grid):
    data = createData(grid)
    data = groupByAngle(data)
    shootEm(data)

def main():
    data = realData

    rows = data.split('\n')
    grid = []
    for row in rows:
        grid.append(list(row))
    resolve(grid)





realData = "##.#..#..###.####...######\n\
#..#####...###.###..#.###.\n\
..#.#####....####.#.#...##\n\
.##..#.#....##..##.#.#....\n\
#.####...#.###..#.##.#..#.\n\
..#..#.#######.####...#.##\n\
#...####.#...#.#####..#.#.\n\
.#..#.##.#....########..##\n\
......##.####.#.##....####\n\
.##.#....#####.####.#.####\n\
..#.#.#.#....#....##.#....\n\
....#######..#.##.#.##.###\n\
###.#######.#..#########..\n\
###.#.#..#....#..#.##..##.\n\
#####.#..#.#..###.#.##.###\n\
.#####.#####....#..###...#\n\
##.#.......###.##.#.##....\n\
...#.#.#.###.#.#..##..####\n\
#....#####.##.###...####.#\n\
#.##.#.######.##..#####.##\n\
#.###.##..##.##.#.###..###\n\
#.####..######...#...#####\n\
#..#..########.#.#...#..##\n\
.##..#.####....#..#..#....\n\
.###.##..#####...###.#.#.#\n\
.##..######...###..#####.#"

test1 = ".#..#\n\
.....\n\
#####\n\
....#\n\
...##"

test2 = "......#.#.\n\
#..#.#....\n\
..#######.\n\
.#.#.###..\n\
.#..#.....\n\
..#....#.#\n\
#..#....#.\n\
.##.#..###\n\
##...#..#.\n\
.#....####"

test3 = "#.#...#.#.\n\
.###....#.\n\
.#....#...\n\
##.#.#.#.#\n\
....#.#.#.\n\
.##..###.#\n\
..#...##..\n\
..##....##\n\
......#...\n\
.####.###."

test4 = ".#..#..###\n\
####.###.#\n\
....###.#.\n\
..###.##.#\n\
##.##.#.#.\n\
....###..#\n\
..#.#..#.#\n\
#..#.#.###\n\
.##...##.#\n\
.....#.#.."

test5 = ".#..##.###...#######\n\
##.############..##.\n\
.#.######.########.#\n\
.###.#######.####.#.\n\
#####.##.#.##.###.##\n\
..#####..#.#########\n\
####################\n\
#.####....###.#.#.##\n\
##.#################\n\
#####.##.###..####..\n\
..######..##.#######\n\
####.##.####...##..#\n\
.#####..#.######.###\n\
##...#.##########...\n\
#.##########.#######\n\
.####.#.###.###.#.##\n\
....##.##.###..#####\n\
.#.#.###########.###\n\
#.#.#.#####.####.###\n\
###.##.####.##.#..##"

test6 = ".#....#####...#..\n\
##...##.#####..##\n\
##...#...#.#####.\n\
..#.....X...###..\n\
..#.#.....#....##"

main()