def main(): 
    spacecraft = {"name": "James Webb Space Telescope"}         # 1. way to create a dictionary
    spacecraft["distance"] = 0.01                               # 2. way to add a single dictionary
    spacecraft.update({"orbit": "Sun", "height": "Unknown"})    # 3. way to add multiple dictionaries
    print(create_report(spacecraft))

def create_report(spacecraft):
    return f"""
    ========= REPORT =========

    Name: {spacecraft.get("name", "Unknown")}
    Distance: {spacecraft.get("distance", "Unknown")} AU
    Orbit: {spacecraft.get("orbit", "Unknown")}

    ==========================
    """

main()

# .get() allows you to add a second string that returns, if it can't find that dictionary