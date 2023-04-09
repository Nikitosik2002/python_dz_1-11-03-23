class TypeMeta(type):
    single_obj = None

    def __call__(cls, *args, **kwargs):
        if cls.single_obj == None:
            cls.single_obj = super().__call__(*args)
        return cls.single_obj


class MyClass(metaclass=TypeMeta):
    def __init__(self):
        pass


obj = MyClass()
obj_2 = MyClass()
obj_3 = MyClass()

print(obj is obj_2)
print(obj_2 is obj_3)
print(obj is obj_3)
