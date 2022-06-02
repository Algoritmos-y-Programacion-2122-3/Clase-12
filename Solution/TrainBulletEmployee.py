from Employee import Employee


class TrainBulletEmployee(Employee):

    rate = 60
    train_type = "Bullet"

    def __init__(self, name, dni, hours):
        super().__init__(name, dni, hours)

    def calculate_rate(self):
        if self.hours > 8:
            return self.hours * (1 + 0.30) * TrainBulletEmployee.rate
        return self.hours * TrainBulletEmployee.rate

    def show_attr(self):
        return f'Nombre: {self.name}|DNI: {self.dni}|Horas: {self.hours} | Monto: ${self.calculate_rate()} | Tipo de Tren: {self.train_type}'
