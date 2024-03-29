import math

class Part:
    def __init__(self, text):
        text = text.strip()
        vals = text.split(' ')
        self.count = int(vals[0])
        self.type = vals[1]

    def toString(self):
        return str(self.count) + " " + self.type

class Formula:
    def __init__(self, text):
        self.ingredients = []
        values = text.split("=>")
        self.output = Part(values.pop().strip())

        inps = values[0].strip()
        for inp in inps.split(', '):
            self.ingredients.append(Part(inp))

    def toString(self):
        text = ""
        for ing in self.ingredients:
            text += ing.toString() + " "
        text += "=> " + self.output.toString()
        return text

class RecipeBook:
    def __init__(self, data):
        self.sourceFormulas = {}
        for d in data:
            f = Formula(d)
            self.sourceFormulas[f.output.type] = f

    def create(self, target, targetCount, leftovers):
        if target == "ORE":
            return targetCount

        #print("Need " + str(targetCount) + " " + target)

        recipe = self.sourceFormulas[target]
        #print(recipe.toString())
        output = recipe.output
        #print("calcing multi for " + target + ": " + str(targetCount) + " / " + str(output.count))
        multi = math.ceil(targetCount / output.count) # how many times do we need this recipe
        #print(multi)

        produced = output.count * multi
        if produced > targetCount:
            #print("Storing " + str(produced - targetCount) + " leftovers")
            if output.type not in leftovers:
                leftovers[output.type] = 0
            leftovers[output.type] += produced - targetCount

        sum = 0
        for ingredient in recipe.ingredients:
            count = ingredient.count * multi
            type = ingredient.type
            if type in leftovers:
                print("using " + str(leftovers[type]) + " leftovers")
                if leftovers[type] >= count:
                    leftovers[type] -= count
                    continue
                else: # not enough left
                    count -= leftovers[type]
                    leftovers[type] = 0
            #print("still need " + str(count) + " " + type)
            sum += self.create(ingredient.type, count, leftovers)
            #print("Sum after " + ingredient.type + " is now " + str(sum) + ", multi is " + str(multi))

        print(leftovers)
        return sum

def main():
    rb = RecipeBook(data)
    print(rb.create("FUEL", 1, {}))

data = [
    "118 ORE => 7 GTPZ",
    "6 RNQJN, 4 NQKVW => 4 DTQRC",
    "2 GBXJL => 3 XHBR",
    "4 BPZM => 9 LVDRH",
    "131 ORE => 3 RHBL",
    "2 LFZS => 2 FPRJW",
    "6 GTPZ => 4 VTBTK",
    "8 GPMP, 2 BPNFJ, 3 LFZS => 2 SFGCR",
    "3 GPMP => 4 SPRCM",
    "16 XCDZP, 1 NQKSL => 4 NQKVW",
    "2 BXGD, 3 VJHSV, 1 MGNCW => 8 MGLH",
    "1 XLNTJ => 1 KXBGP",
    "9 PJQWR, 19 NQKVW, 10 GJHWN => 7 ZBGDF",
    "3 VTBTK => 6 CJNQ",
    "12 PJQWR => 1 JNHBR",
    "16 BPZM => 9 MVCH",
    "1 KWPXQ, 1 LVDRH => 6 LFZS",
    "6 VTBTK => 6 XCDZP",
    "1 PZFG, 2 LFZS, 2 CJNQ, 2 FPRJW, 17 MVCH, 7 MGNCW, 26 KXBGP => 6 TBTL",
    "2 DTQRC, 7 NBNLC => 8 BPZM",
    "102 ORE => 3 WNTQ",
    "1 WNTQ => 9 NQKSL",
    "5 XZMH, 1 LPLMR, 13 BXGD => 8 JPFL",
    "1 NQKSL, 6 XCDZP, 2 FCDVQ => 9 GJHWN",
    "6 XZMH => 4 GLDL",
    "23 ZTWR, 4 BPZM => 2 MGNCW",
    "11 GPMP, 19 ZBGDF => 2 XZMH",
    "2 MGNCW, 4 XCDZP, 17 KQLT => 4 VJHSV",
    "1 CJNQ => 7 QHPH",
    "1 RHBL => 8 GBXJL",
    "2 MVCH, 3 KDNT, 6 NBNLC, 26 QHPH, 2 KRKB, 1 MCPDH, 4 XZMH, 6 XHBR => 1 HZMWJ",
    "9 XDLZ => 1 QSXKS",
    "4 GLDL => 6 WJNP",
    "5 MVCH => 3 MCPDH",
    "14 TKGM => 5 LPLMR",
    "1 WVQN => 2 PJQWR",
    "4 KWPXQ => 6 FCDVQ",
    "10 DTQRC, 27 TBTL, 9 HZMWJ, 41 XVGP, 2 TPZFL, 54 WNTQ, 85 RHBL, 5 WCZK, 2 QVSB, 28 SPRCM => 1 FUEL",
    "15 RNQJN, 1 PJQWR, 2 NBNLC => 4 TKGM",
    "126 ORE => 5 WVQN",
    "10 NBNLC => 3 BWMD",
    "2 SFGCR, 1 NQKSL, 1 KRKB => 1 WGQTF",
    "2 MLWN => 5 ZTWR",
    "12 DTQRC, 3 NQKVW, 9 NBNLC => 8 BPNFJ",
    "10 SFGCR, 1 PZFG, 2 ZVFVH, 12 WJNP, 14 WGQTF, 1 JNHBR, 8 FPRJW => 3 QVSB",
    "2 MCPDH => 8 XVGP",
    "19 JPFL => 4 TPZFL",
    "5 GBXJL => 6 MLWN",
    "9 TKGM => 5 KDNT",
    "1 NQKVW, 15 PJQWR => 9 XDLZ",
    "2 QHPH, 2 JNHBR => 1 ZVFVH",
    "189 ORE => 6 KWPXQ",
    "5 KRKB, 3 MGLH => 6 WCZK",
    "3 NBNLC, 8 BWMD => 7 KRKB",
    "1 ZBGDF, 6 XDLZ => 4 GPMP",
    "11 XDLZ, 1 QSXKS => 2 BXGD",
    "2 KRKB, 1 GJHWN => 1 XLNTJ",
    "3 ZTWR => 4 RNQJN",
    "15 FCDVQ, 3 MLWN => 4 NBNLC",
    "1 KDNT, 1 XZMH, 8 BXGD => 1 KQLT",
    "2 WJNP => 3 PZFG",
]

test = [
    "10 ORE => 10 A",
    "1 ORE => 1 B",
    "7 A, 1 B => 1 C",
    "7 A, 1 C => 1 D",
    "7 A, 1 D => 1 E",
    "7 A, 1 E => 1 FUEL",
]

test2 = [
    "9 ORE => 2 A",
    "8 ORE => 3 B",
    "7 ORE => 5 C",
    "3 A, 4 B => 1 AB",
    "5 B, 7 C => 1 BC",
    "4 C, 1 A => 1 CA",
    "2 AB, 3 BC, 4 CA => 1 FUEL",
]

main()
