def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts



coins = {"galleons": 100, "sickles": 50, "knuts": 25}

print(total(coins["galleons"], coins["sickles"], coins["knuts"]), "Knuts")

# Also a very good solution for our problem, which might solve the sorting problem
# But for endless long dictionaries it will still become complicated

