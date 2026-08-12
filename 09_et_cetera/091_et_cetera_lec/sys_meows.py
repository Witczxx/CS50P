import sys

if len(sys.argv) == 1:
    print('meow')
elif len(sys.argv) == 3 and sys.argv[1] == '-n':
    n = int(sys.argv[2])
    for _ in range(n):
        print('meow')
    
else:
    print('usage: sys_meows.py')


# we use sys.argv by adding -n
# this says to add this argument multiple times
