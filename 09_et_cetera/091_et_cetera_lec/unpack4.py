def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts



coins = {"galleons": 100, "sickles": 50, "knuts": 25}

print(total(**coins), "Knuts")

# Genius! It will perform following steps now
# Into the parenthesis, it will write:
# galleons = 100, sickles = 50, knutes = 25

