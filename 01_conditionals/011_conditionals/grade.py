score = int(input("Score: "))

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")


"""
Alternatives:
Before we were using "and" to connect the scores in a condition - but in python it can be eliminated.
We can skip using "and" by just putting the symbols around the variable - "100 >= score >= 90" .
"""
