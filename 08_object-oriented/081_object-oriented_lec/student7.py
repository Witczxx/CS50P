# __init__: In case someone constructs following variables (name, house), a process is initialized.
class Student:
    def __init__(self, name, house, patronus):
        if not name:
            raise ValueError("Missing Name.")
        if house not in ["Gryffindor", "Huffelpuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid House.")
        self.name = name
        self.house = house
        self.patronus = patronus

# __str__: In case sth triggers the class as a string (like print), you can choose what to happen
    def __str__(self):
        return f"{self.name} from {self.house}"

# You can create your own functions!
    def charm(self):
        match self.patronus:
            case "Stag":
                return "Horse-Emoji"
            case "Otter":
                return "Otter-Emoji"
            case "Jack Russel Terrier":
                return "Dog-Emoji"
            case _:
                return "/"

def main():
    student = get_student()
    print("Expecto Patronum!")
    print(student.charm())


def get_student():
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ")
    return Student(name, house, patronus)


if __name__ == "__main__":
    main()
