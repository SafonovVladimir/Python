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


class ElectroCar(CarsClass):
    '''
    Клас електромашинб ініціалізація атрибутів
    '''
    def __init__(self, brand, model, year, probeg):
        super().__init__(brand, model, year, probeg)



s_car = CarsClass('Ferrari', 'F1', '2022', '10')

s_car.showCar()
s_car.drowCar(50)
s_car.showCar()