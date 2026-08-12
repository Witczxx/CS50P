# E = mc2 - prompt for mass
# c ~ 300000000 m/s

def formula(s):
    s = int(s)
    return s * 300000000 * 300000000

print(formula(input("m: ")))