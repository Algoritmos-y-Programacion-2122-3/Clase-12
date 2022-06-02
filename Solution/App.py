from TrainCoalEmployee import TrainCoalEmployee as Coal
from TrainBulletEmployee import TrainBulletEmployee as Bullet


class App():

    def __init__(self):
        self.employees = []

    def register(self):
        name = input("Ingrese su nombre: ")
        dni = input("Ingrese su cedula: ")
        while True:
            try:
                hours = int(input("Ingrese las horas: "))
                train_type = input("Tipo de tren (1)Carbon, (2)Supersonico: ")
                if train_type != "1" and train_type != "2":
                    raise Exception
                break
            except:
                print("Error!")

        if train_type == "1":
            employee = Coal(name, dni, hours)
            # name: pepito, dni: 123, hours: 15, rate: 30, type: coal
        else:
            employee = Bullet(name, dni, hours)
            # name: maria, dni: 542, hours: 2, rate: 60, type: bullet

        self.employees.append(employee)
        print("Empleado registrado exitosamente")
        print(employee.show_attr())

    def show_employees(self):
        for employee in self.employees:
            print(employee.show_attr())

        print(f"La cantidad total es de {len(self.employees)}")

    def employee_by_train_type(self):

        coal_employees = list(
            filter(lambda employee: employee.train_type == "Coal", self.employees))

        bullet_employees = list(
            filter(lambda employee: employee.train_type == "Bullet", self.employees))

        print(
            f"La cantidad de empleados en tren de carbon es de {len(coal_employees)}")
        print(
            f"La cantidad de empleados en tren de supersonico es de {len(bullet_employees)}")

    def employee_by_increase(self):

        employee_with_bonus = list(
            filter(lambda employee: employee.hours > 8, self.employees))

        print(
            f"La cantidad de empleados con aumento es de {len(employee_with_bonus)}")

    def average_payments(self):
        coal_employees = list(
            filter(lambda employee: employee.train_type == "Coal", self.employees))

        bullet_employees = list(
            filter(lambda employee: employee.train_type == "Bullet", self.employees))

        coal_employees_amounts = list(
            map(lambda employee: employee.calculate_rate(), coal_employees))

        bullet_employees_amounts = list(
            map(lambda employee: employee.calculate_rate(), bullet_employees))

        if len(coal_employees_amounts) > 0:
            print(
                f"El promedio de pago de los trenes de carbon es de {sum(coal_employees_amounts)/len(coal_employees_amounts)}")
        else:
            print("No hay datos registrados en trenes de carbon")

        if len(bullet_employees_amounts) > 0:
            print(
                f"El promedio de pago de los trenes supersonicos es de {sum(bullet_employees_amounts)/len(bullet_employees_amounts)}")
        else:
            print("No hay datos registrados en trenes supersonicos")

    def best_employee(self):
        best_employee = self.employees[0]
        for employee in self.employees:
            # if best_employee == 0:
            #     best_employee = employee
            if employee.calculate_rate() > best_employee.calculate_rate():
                best_employee = employee
        print(f"El mejor empleado es {best_employee.dni}")

    def stadistics(self):
        while True:
            opcion = input("""
            1)La cantidad total de personal con su información
            2)La cantidad de personal por tipo de tren
            3)La cantidad de personal a quienes se les otorgó el aumento
            4)El Promedio de pago por tipo de tren
            5)Empleado del mes
            6) Salir de estadisticas
            > """)
            if opcion == "1":
                self.show_employees()
            elif opcion == "2":
                self.employee_by_train_type()
            elif opcion == "3":
                self.employee_by_increase()
            elif opcion == "4":
                self.average_payments()
            elif opcion == "5":
                self.best_employee()
            else:
                break

    def start(self):
        while True:
            opcion = input("""Bienvenido a Saman Train
            1) Registro
            2) Estadisticas
            3) Salir
            > """)
            if opcion == "1":
                self.register()
            elif opcion == "2":
                self.stadistics()
            else:
                print("Adios!")
                break
