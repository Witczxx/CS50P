# Tuple: x, y
# A Collection of Values (not list, because unmutable)
# In Lists, you can change the values
# In Tuples, you can't change the values like that (more simple)
# The Parenthesis for Tuples are Optional

def main():
    student = get_student()
    print(f"{student[0]} from {student[1]}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return (name, house)

if __name__ == "__main__":
    main()
