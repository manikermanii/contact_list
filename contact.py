
class Contact:
    def __init__(self, name, family, title, number):
        self.name = name
        self.family = family 
        self.email = title
        self.address = number

    def to_tuple(self):
        return (self.name, self.family, self.email, self.address)




