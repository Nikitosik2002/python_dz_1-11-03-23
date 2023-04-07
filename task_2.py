class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def counting(self):
        print(f"{obj._length * obj._width * 25 * 0.05} т")


obj = Road(length=int(input("Введите длинну покрытия: ")),
           width=int(input("Введите ширину покрытия: ")))
obj.counting()
