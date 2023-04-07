class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def get_full_name(self):
        print(self.name, self.surname, self.position, sep="\n")

    def get_total_income(self):
        print(self._income.get("wage") + self._income.get("bonus"))


obj = Position("Алеша", "Попович", "Богатырь", {"wage": 40000, "bonus": 6000})
obj.get_full_name()
obj.get_total_income()
