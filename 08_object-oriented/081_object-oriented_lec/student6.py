# Talking about Methods - Classes come with Methods (Functions) inside of them


class Student:
    def __init__(self, name, house):
        # self (can be anything) makes sure, there is some self-initiation
        # it created a memory for us and inside we can fill it with content
        self.name = name
        self.house = house

def main():
    student = get_student()
    print(f"{student.name} from {student.house}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    # More Powerful this way - we have more control and can modify the data more
    # It is called a Constructor Call - Telling to Construct/Instanciate 2 Objects for me
    # It is using Student Class as a Mold
    return Student(name, house)

if __name__ == "__main__":
    main()
