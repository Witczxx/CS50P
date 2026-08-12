with open("names.txt", "r") as file:
    for line in file:
        print("hello", line.rstrip())  # most elegant solution
    # But here - you can not sort things now! - so maybe names 3 is better ? :D Let's check on names5
