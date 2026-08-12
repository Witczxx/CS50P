results = ["Mario", "Luigi"]

results.append("Princess")                          # append() adds new values into the list
results.append("Yoshi")
results.append("Koopa Troopa")
results.append("Toad")

results.append(["Bowser", "Donkey Kong Jr."])       # does not work for multiple values
results.remove(["Bowser", "Donkey Kong Jr."])       # removes values
results.extend(["Bowser", "Donkey Kong Jr."])       # works for multiple values

print (results)