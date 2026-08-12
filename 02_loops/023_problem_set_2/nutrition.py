fruit_table = [
    {"Fruit": "Apple", "Calories": 130},
    {"Fruit": "Avocado", "Calories": 50},
    {"Fruit": "Banana", "Calories": 110},
    {"Fruit": "Cantaloupe", "Calories": 50},
    {"Fruit": "Grapefruit", "Calories": 60},
    {"Fruit": "Grapes", "Calories": 90},
    {"Fruit": "Honeydew Melon", "Calories": 90} ,
    {"Fruit": "Kiwifruit", "Calories": 50},
    {"Fruit": "Lemon", "Calories": 15},
    {"Fruit": "Lime", "Calories": 20},
    {"Fruit": "Nectarine", "Calories": 60},
    {"Fruit": "Orange", "Calories": 80},
    {"Fruit": "Peach", "Calories": 60},
    {"Fruit": "Pear", "Calories": 100},
    {"Fruit": "Pineapple", "Calories": 50},
    {"Fruit": "Plums", "Calories": 70},
    {"Fruit": "Starwberries", "Calories": 50},
    {"Fruit": "Sweet Cherries", "Calories": 100},
    {"Fruit": "Tangerine", "Calories": 50,},
    {"Fruit": "Watermelon", "Calories": 80}
    ]


def main():
    item = input("Item: ").title()
    calories = check_calories(item)
    if calories != "":
        print(f"Calories: {calories}")
    else:
        print("", end="") 


def check_calories(s):
    for n in range(len(fruit_table)):
        if s == fruit_table[n]["Fruit"]:
            return fruit_table[n]["Calories"]
        else:
            pass
    return ""

main()


