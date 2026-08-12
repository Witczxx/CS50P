"""
# Creating a Class
class Student:
    ...

def main():
    student = get_student()
    print(f"{student.name} from {student.house}")

def get_student():
    # Creating an Object
    student = Student()
    # Creating Attributes (Instance Variables)
    student.name = input("Name: ")
    student.house = input("House: ")
    return student

if __name__ == "__main__":
    main()
"""
