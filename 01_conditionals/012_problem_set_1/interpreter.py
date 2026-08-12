# float allows unwhole numbers
# x is an integer
# z is an integer
# y is +/-/* or /

def cal(s):

    x = int(s[0])
    y = s[1]
    z = int(s[2])

    if y == "+":
        return x + z
    elif y == "-":
        return x - z
    elif y == "*":
        return x * z
    elif y == "/":
        if z == 0:
            return "error"
        else:
            return x / z
    else:
        return "error2"

equation = input("Expression: ").split(" ")

if cal(equation) == "error":
    print("Don't divide by 0")
elif cal(equation) == "error2":
    print("Wrong Expression")
else:
    print(float(cal(equation)))