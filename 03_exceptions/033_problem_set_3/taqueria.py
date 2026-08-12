menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}


def main():
    total = 0
    while total >= 0:
        prize = take_and_calculate("Item: ")
        try:
            total = total + prize
        except TypeError:
            break
        print(f"${total}")

        



def take_and_calculate(prompt):
    while True:
        try:
            meal_name = input(prompt).title()       # Take
            meal_prize = menu[meal_name]    # Calculate
            return meal_prize
        except KeyError:
            pass
        except EOFError:
            break


main()