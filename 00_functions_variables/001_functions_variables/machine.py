emoticon = "v.v"

def main():
    global emoticon
    say("Is anyone here?")
    emoticon = ":D"
    say("Oh, hi.")


def say(phrase):
    print(phrase + " " + emoticon)


main()


### We designed a side effect - a modification of print() adding a smiley.
### Usually we can only access global varibles within a "def" scope.
### To modify it -> use "global"