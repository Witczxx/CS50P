# We can not create new variables in every while loop
# But we can add a new entry each time into a dictionary

counts = {}
groceries = []

def main():

    while True:
        try:
            groceries.append(input().upper())
        except EOFError:
            break

    print("") # Start in a new line
    sorted_groceries = sorted(groceries)

    for grocery in sorted_groceries:
        if grocery in counts:
            counts[grocery] += 1
        else:
            counts[grocery] = 1

    for grocery in counts:
        print(f"{counts[grocery]} {grocery}")

main()