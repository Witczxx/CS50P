import sys

## imported from python file in same directory
# it is ignoring the main(), so just getting what we need ! !

from sayings import goodbye 

if len(sys.argv) == 2:
    goodbye(sys.argv[1])