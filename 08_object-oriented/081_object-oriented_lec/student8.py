# Let's talk about Properties (which are functions) and how to Decorate them

# You can not call The Variable and the Function house!

class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing Name.")
        self.name = name
        # No Underscore Changing! Otherway no Error Cecking! :
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    # Getter
    @property
    def house(self):
        return self._house

    # Putting the ValueError here has the advantage
    # That even when the Programmer makes changes, the Error is working
    # in __init__ the inputs are not safe from Errors by Programmers
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Huffelpuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid House.")
        self._house = house

# Seeing the function .house for the first time straightly triggers the setter
def main():
    student = get_student()
    # Because of here - now there will be a ValueError - even though your inputs are correct!
    # L> student._house = "Number Four, Privet Drive"
    print(student)


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)


if __name__ == "__main__":
    main()
