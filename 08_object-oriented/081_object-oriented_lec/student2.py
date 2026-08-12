# Because Tuples can not be edited, we had to change into lists
# It is not a limitation, it is a certain feature we might need sometimes

def main():
    student = get_student()
    if student[0] == "Padma":
        student[1] = 'Ravenclaw'
    print(f"{student[0]} from {student[1]}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return [name, house]

if __name__ == "__main__":
    main()
