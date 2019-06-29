class Airplane():
    def __init__(self, make, model, year, max_speed):
        self.make = make
        self.model = model
        self.year = year
        self.odometr = 0
        self.is_flying = False
        self.max_speed = max_speed

    def take_off(self):
        self.is_flying = True
        print(self.is_flying)  

    def land(self):
        self.is_flying = False
        print(self.is_flying)

    def fly(self, distrance):
        if distrance != 0:
            self.odometr += distrance 
        print("This plane has " + str(self.odometr) + " miles on it.")

ata = Airplane('Ridus', 'Su-35C', 2018, 0)
print('----------------Первоначальное состояние----------------')
print(ata.is_flying)
print('-----------------------Взлет----------------------------')
ata.take_off()
ata.fly(2500)
ata.fly(50)
print('-----------------------Приземление----------------------')
ata.land()
