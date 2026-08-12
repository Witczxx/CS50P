# Hypothetical - Keep Checking the Soil Wet Percentage to know when to water the Plant

from soil import sample

def main():
    moisture = sample()
    days = 0
    print(f"Days {days}: Moisture is {moisture}%")

    while moisture > 20:                    # While Sample is wet - it will keep running
        moisture = sample()                 # As long as the condition is true
        days += 1                           # Good when we don't know how long it will be true
        print(f"Moisture is {moisture}%")
    print("Time to Water!")

main()