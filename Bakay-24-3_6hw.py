class Hero:
    def __init__(self, agility=0, strenght=0, intelligence=0, power=0):
        self.__agility = agility
        self.__strenght = strenght
        self.__intelligence = intelligence
        self.__power = power

    def setglty(self, agility):
        self.__agility = agility

    def getglty(self):
        return self.__agility

    def setstr(self, strenght):
        self.__strenght = strenght

    def getstr(self):
        return self.__strenght

    def setint(self, intelligence):
        self.__intelligence = intelligence

    def getint(self):
        return self.__intelligence

    def setpwr(self, power):
        self.__power = power

    def getpwr(self):
        return self.__power


superhero = Hero()
superhero.setglty(65)
superhero.setstr(100)
superhero.setint(30)
superhero.setpwr(50)
print(f'Ловкость {superhero.getglty()}\n'
      f'Сила {superhero.getstr()}\n'
      f'Интеллект {superhero.getint()}\n'
      f'Мощь {superhero.getpwr()}\n')
