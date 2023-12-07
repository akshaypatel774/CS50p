from datetime import date, datetime
import sys
import inflect

class dateOfBirth:
    def __init__(self, birthdate=None):
        self.today = self.current_date()
        self.birthdate = self.valid_date(birthdate)
        self.difference = self.difference()

    def __str__(self):
        return str(self.birthdate)

    def current_date(self):
        return datetime.combine(date.today(), datetime.min.time())

    def valid_date(self, birthdate):
        if birthdate == None:
            birthdate = input("Date of Birth: ")
        try:
            dob_date = datetime.strptime(birthdate, "%Y-%m-%d").date()
            dob_datetime = datetime(dob_date.year, dob_date.month, dob_date.day)
            return dob_datetime
        except ValueError:
            sys.exit("Invalid Date format")

    def difference(self):
        return int((self.today - self.birthdate).total_seconds()/60)


def main():
    dateofbirth = dateOfBirth()
    print(sing(dateofbirth.difference))

def sing(minutes):
    p = inflect.engine()
    lyrics = p.number_to_words(minutes, andword="")
    lyrics = f"{lyrics} minutes".capitalize()
    return lyrics


if __name__ == "__main__":
    main()