'''
Use a última versão de electric_car.py desta seção.
Acrescente um método chamado upgrade_battery() na classe Battery. Esse método deve verificar a capacidade da bateria e defini-la com 85 se o valor for diferente. Crie um carro elétrico com uma capacidade de bateria default, chame get_range() uma vez e, em seguida, chame get_range() uma segunda vez após fazer um upgrade da bateria. Você deverá ver um aumento na distância que o carro é capaz de percorrer.
'''

class Car():

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class Battery():
    
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a " + str(self.baterry_size) + "-kWh battery.")

    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "This car can go approximately " + str(range) + " miles on a full charge."
        print(message)

    # Única função acrescentada do código presente no livro
    def upgrade_battery(self):
        if self.battery_size != 85:
            self.battery_size = 85

class ElectricCar(Car):

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.baterry = Battery()


# Linhas de comando acrescentadas em relação ao livro
tesla = ElectricCar('tesla', 'model s', 2016)    
tesla.baterry.get_range()
tesla.baterry.upgrade_battery()
tesla.baterry.get_range()
