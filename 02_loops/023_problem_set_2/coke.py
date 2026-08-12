def main():

    due = 50        # Cola Prize

    while due > 0:
        print(f"Amount Due: {due}")         # Presenting Cola Prize
        coin = int(input("Insert Coin: "))  # Coin Input

        if coin == 5 or coin == 10 or coin == 25:       # Suitable Coins
            due = due - coin                        # Coin Subtraction
        else:
            pass                                    # If unvalid coin
    
    if due < 0:
        due = due - (due * 2)                       # converting negative to positive number
    else:
        pass                                        # if positive number

    print(f"Change Owed: {due}")                    # return owed money



main()



"""
def main():
    due = 50
    print(f"Amount Due: {due}")
    coin = int(input("Insert Coin: "))
    insert(coin)
    print(f"Change Owed: {due}")

def inert(money):
    while due > 0:
        if money == 5 or coin == 10 or coin == 25:
            due = due - money
        else:
            pass

main()
"""