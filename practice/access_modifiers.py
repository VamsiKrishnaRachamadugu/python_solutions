class A:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def _assign_values_method(self):
        # self.name=name
        return self.name


class B(A):
    def __init__(self, id, name, age, salary):
        super().__init__(name, salary)
        self._id = id
        self.age = age


class C(B):
    def __init__(self, id, name, age, salary, level):
        super().__init__(id, name, age, salary)
        self.level = level
    try:
        def display(self):
            print(self._id, self.age, self.name, self.__salary, self.level)
    except AttributeError as e:
        print(e)
        print('Caught Exception' )

obj = C(1, 'vamsi', 22, 2000, 'ASE')
obj.display()
# print(obj._assign_values_method())

# class Employee:
#     # constructor
#     def __init__(self, name, sal):
#         self._name = name  # protected attribute
#         self.__sal = sal
#
#
# class HR(Employee):
#
#     # member function task
#     def task(self):
#         print("We manage Employees")
#
#
# hr_emp = HR('vamsi', 2200)
# print(hr_emp._sal)
