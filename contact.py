
class Contact :
    def __init__(self, name, family, title, number):
        self.name = name
        self.phone = family
        self.email = title
        self.address = number 

    def __str__(self):
        return f"{self.name} {self.family} {self.title} {self.number}"

    def to_tuple(self):
        return self.name, self.family, self.title, self.number



