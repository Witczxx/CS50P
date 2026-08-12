written_months = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}

def main():
    raw_date = get_date("Date: ") 
    converted_date = convert_date(raw_date)
    print(converted_date)


def get_date(prompt):
    while True:
        raw = input(prompt)

        if raw[-5] == "/":  # Goal: Only Input (M)M/(D)D/YYYY 
            raw_parts = raw.split("/")
            if int(raw_parts[0]) <= 12 and int(raw_parts[1]) <= 31 and int(raw_parts[2]) <= 9999:
                return raw_parts
            else:
                pass

        elif raw[-6] == ",":  # Goal: Only Input "Month" (D)D, YYYY
            raw_parts = raw.split(" ")
            day = raw_parts[1]
            raw_parts[1] = day[:-1]
            if raw_parts[0] in written_months and int(raw_parts[1]) <= 31 and int(raw_parts[2]) <= 9999:
                return raw_parts
            else:
                pass

        else: # If input doesn't meet criteria, ask for retry
            pass


def convert_date(d):    # Conversion into YYYY-MM-DD

    if d[0] in written_months:
        return f"{d[2]}-{written_months[d[0]]}-{d[1]}"

    else:
        return f"{d[2]}-{d[0]}-{d[1]}"


main()
