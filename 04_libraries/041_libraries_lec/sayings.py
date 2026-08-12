def main():
    hello("world")
    goodbye("world")

def hello(name):
    print(f"hello, {name}")

def goodbye(name):
    print(f"goodbye, {name}")

if __name__ == "__main__":      # Needed for sayings_v2.py to work!!
    main()                      # otherway it will run main() and nothing works!!