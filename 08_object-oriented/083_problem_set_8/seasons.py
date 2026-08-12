import datetime as dt
import num2words as n2w
import sys

class Birthday:

    def __init__(self, bday=None):
        self.bday = bday

    def __str__(self):
        return f"{self.dif_minutes_words} minutes"

    # Subtracts the Dates of Today and Input, resulting in a TimeDelta Class
    def date_dif(self):
        delta = dt.date.today() - self.bday
        self.dif_minutes = delta.days * 24 * 60
        return self

    # Uses N2W to convert the dif_min int() into Words
    def convert_to_words(self):
        self.dif_minutes_words = n2w.num2words(self.dif_minutes)
        self.dif_minutes_words = self.dif_minutes_words.replace("and ", "")
        return self

    @property
    def bday(self):
        return self._bday

    # Checks the Format of the Input, before accpeting it
    @bday.setter
    def bday(self, bday):
        try:
            self._bday = dt.date.strptime(bday, "%Y-%m-%d")
        except ValueError:
            sys.exit("Invalid Date.")


# Uses all Class-Functions in one Chain
def main():
    bday = input("Enter your Birthday (YYYY-MM-DD): ")
    bday_converted = Birthday(bday).date_dif().convert_to_words()
    print(bday_converted)


if __name__ == "__main__":
    main()

