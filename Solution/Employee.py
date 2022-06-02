
class Employee():

    def __init__(self, name, dni, hours):
        self.name = name
        self.dni = dni
        self.hours = hours

    def show_attr(self):
        return f'{self.dni}'

    def calculate_rate(self):
        pass
