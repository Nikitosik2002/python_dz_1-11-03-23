class Matrix:

    def __init__(self, array=None):
        self.array = array
        if array is None:
            print("Нет аргументов")
        else:
            pass
    def __add__(self, other):
        result = [[self.array[i][j] + other.array[i][j]
                   for j in range(len(self.array[0]))]
                  for i in range(len(self.array))]
        return result
    def __str__(self):
        res = ""
        for el in self.array:
            res += (f"{el}\n")
        return res


obj_1 = Matrix(((4, 3), (2, 1)))
obj_2 = Matrix(((1, 2), (3, 4)))
print(obj_1)
print(obj_2)
print(obj_1 + obj_2)

