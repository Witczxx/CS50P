import datetime as dt

from num2words import num2words


class BirthdayCounter:
    def __init__(self, bday_str):
        self.bday = self._validate_and_parse(bday_str)

    def _validate_and_parse(self, bday_str):
        try:
            return dt.datetime.strptime(bday_str, "%Y-%m-%d").astimezone().date()
        except ValueError:
            raise ValueError("Ungültiges Format. Bitte YYYY-MM-DD verwenden.")

    def get_total_minutes_in_words(self):
        today = dt.datetime.now(dt.timezone.utc).date()
        total_days = today - self.bday
        total_minutes = total_days.days * 24 * 60
        minutes_in_words = num2words(total_minutes).replace("and ", "")
        return minutes_in_words

    def __str__(self):
        minutes_in_words = self.get_total_minutes_in_words()
        return f"{minutes_in_words} minutes."


def get_birthday():
    dob = input("Date of Birth (YYYY-MM-DD): ")
    return dob


def main():
    dob_string = get_birthday()

    try:
        counter = BirthdayCounter(dob_string)
        print(counter)

    except ValueError as error_message:
        print(f"Fehler: {error_message}")


if __name__ == "__main__":
    main()
