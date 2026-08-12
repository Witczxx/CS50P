import cowsay
import sys


# Sys is cool for allowing to make things more quickly as a coder
# You don't ahve to enter the input each time - you just do it all before
if len(sys.argv) == 2:
    cowsay.trex("hello, " + sys.argv[1])

