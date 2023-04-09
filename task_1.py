class TypeField:

    def __set__(self, instance, value):
        if type(value) != str:
            raise ValueError("Тип атрибута может быть только str")

        instance.__dict__[self.atr] = value

    def __set_name__(self, owner, atr):
        self.atr = atr


class WageBonusField:

    def __set__(self, instance, value):
        if type(value.get("wage")) != int or type(value.get("bonus")) != int:
            raise ValueError("Тип атрибута может быть только int")

        if value.get("wage") < 0 or value.get("bonus") < 0:
            raise ValueError("Зарплата или премия "
                             "не могут быть отрицательными")

        if value.get("wage") < value.get("bonus"):
            raise ValueError("Зарплата не может быть ниже премии")

        instance.__dict__[self.atr] = value

    def __set_name__(self, owner, atr):
        self.atr = atr


class Worker:
    name = TypeField()
    surname = TypeField()
    position = TypeField()

    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    _income = WageBonusField()

    def get_full_name(self):
        print(self.name, self.surname, self.position, sep="\n")

    def get_total_income(self):
        print(self._income.get("wage") + self._income.get("bonus"))


obj = Position("asdf", "Попович", "Богатырь", {"wage": 10000, "bonus": 6000})
obj_2 = Position("asdf", "Попович", "Богатырь", {"wage": 10000, "bonus": 6000})
obj.get_full_name()
obj.get_total_income()
print(obj is obj_2)