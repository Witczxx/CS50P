### ask user for their name - remove whitespace from str - capitalize user's name
name = input("What's your name? ").strip().title()

### split user's name into first and last name
first, last = name.split(" ")

### say hello to user
print(f"hello, {first}")



"""
Open File: "code file_name.py" [Terminal]
Run File: "python3 file_name.py" [Terminal]
"""

"""
A "=" is an assignment - much more than an equal sign
It is copying/updating variables from the right to the left
"""

"""
Pseudocode = 1st defining what you want to do with hastags
Then creating the code according to your plan
"""

"""
Code Documentation: https://docs.python.org/3/
2 Options: print(x, y) or print (x + y) 
Option 1 adds a spacebar, while option 2 doesn't
Reason - Documentation: print(*objects, sep=' ', end='\n', file=None, flush=False)
Documentation uses single quotes - but let's just keep using double quote (consistency)
"""