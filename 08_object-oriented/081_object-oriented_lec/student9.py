# Never use _xyz or __xyz Variables of other people

class Student:
    # Triggered by Student(name, house)
    def __init__(self, name, house):
        self.name = name
        self.house = house

    # Triggered by print(student)
    def __str__(self):
        return f"{self.name} from {self.house}"

    @property
    def name(self):
        return self._name

    # Triggered by self.name
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing Name.")
        self._name = name

    @property
    def house(self):
        return self._house

    # Triggered by self.house
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Huffelpuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid House.")
        self._house = house


def main():
    student = get_student()
    print(student)


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)


if __name__ == "__main__":
    main()
