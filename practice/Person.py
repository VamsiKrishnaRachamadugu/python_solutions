class Person:

    def set_name(self, id1, name):
        self.id = id1
        self.name = name

    def get_name(self):
        return self.id, self.name


p = Person()
p.set_name(12, 'Vamsi')
print(p.get_name())
