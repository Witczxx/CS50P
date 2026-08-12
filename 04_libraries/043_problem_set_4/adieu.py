def main():
    name_list = get_names()  # result: variable name_list
    names_with_grammar = add_grammar(name_list)  # result: names with grammar
    print(f"Adieu, Adieu, to {names_with_grammar}.")


def get_names():
    name_list = list()
    while True:
        name_list.append(input("Name: "))
        if "" in name_list:
            name_list.pop()
            return name_list


def add_grammar(name_list):
    if len(name_list) == 1:
        return name_list[0]
    names_with_grammar = [name + "," for name in name_list[:-1]]
    names_with_grammar.append("and " + name_list[-1])
    return " ".join(names_with_grammar)


main()


"""
Less Robust Solution...
    names_with_grammar = list()
    for name in name_list:
        if len(name_list) == 1:
            return name
        elif name != name_list[(len(name_list) - 1)]:
            names_with_grammar.append(name + ",")
        else:
            names_with_grammar.append("and " + name)
            return " ".join(names_with_grammar)
"""
