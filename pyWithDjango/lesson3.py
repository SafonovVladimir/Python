class CarsClass():
    '''
    Клас автомобілей
    '''

    def __init__(self, brand, model, year, probeg):
        '''
        Ініціалізація атрибутів
        '''
        self.brand = brand
        self.model = model
        self.year = year
        self.probeg = int(probeg)

    def showCar(self):
        '''
        Показати інформацію про машину
        '''
        print(f'{self.brand}, {self.model}, '
              f'{self.year} год, {self.probeg} км.')

    def drowCar(self, km):
        '''
        Метод поїздки авто
        '''
        self.probeg = self.probeg + km


class Battery():
    '''
    Клас батареї
    '''

    def __init__(self, battery=100):
        self.battery = battery

    def desc_battery(self):
        print('Цей автомобіль має ємність батареї: ' + str(self.battery) + '%')


class ElectroCar(CarsClass):
    '''
    Клас електромашин, ініціалізація атрибутів
    '''

    def __init__(self, brand, model, year, probeg):
        super().__init__(brand, model, year, probeg)
        self.battery = Battery()  # Значення за замовченням

    # def desc_battery(self):
    #     print('Цей автомобіль має ємність батареї: ' + str(self.battery) + '%')

    # def minus_battery(self, ):


s_car = CarsClass('Ferrari', 'F1', '2022', '10')

# s_car.showCar()
# s_car.drowCar(50)
# s_car.showCar()

# tesla = ElectroCar('Tesla', 'Model S', '2022', 50)
# tesla.showCar()
# tesla.drowCar(100)
# tesla.showCar()
# tesla.desc_battery()


tesla = ElectroCar('Tesla', 'Model S', '2022', 50)
tesla.showCar()
tesla.drowCar(100)
tesla.showCar()
tesla.battery.desc_battery()
