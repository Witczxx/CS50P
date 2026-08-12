def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts

coins = [100, 50, 25]

print(total(coins[0], coins[1], coins[2]), "Knuts")

# This Solution itself is working
# But it can be very 麻烦 to write each time coin0,coin1,coin2
# Therefore we have this possibility to perform "unpacking" -->
