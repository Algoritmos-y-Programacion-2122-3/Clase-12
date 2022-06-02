from Employee import Employee


class TrainCoalEmployee(Employee):

    rate = 30
    train_type = "Coal"

    def __init__(self, name, dni, hours):
        # Employee.__init__(self,name,dni,hours)
        super().__init__(name, dni, hours)

    def calculate_rate(self):
        """Calcula el monto total del empleado carbon

        Returns:
            float: Monto total a pagar del em,pleado
        """
        if self.hours > 8:
            return self.hours * (1 + 0.35) * TrainCoalEmployee.rate
        return self.hours * TrainCoalEmployee.rate

    def show_attr(self):
        return f'Nombre: {self.name}|DNI: {self.dni}|Horas: {self.hours} | Monto: ${self.calculate_rate()} | Tipo de tren: {TrainCoalEmployee.train_type}'
