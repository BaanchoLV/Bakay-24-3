class Hero:
    head=1
    abilyty=True
    def __init__(self,name,nickname,hp,damage):
        self.name=name
        self.nickname=nickname
        self.hp=hp
        self.damage=damage
    def heal(self):
        print(self.hp +100)

    def double_damage(self):
        print(self.damage*2)

    def greetting(self):
        print(f"my name is {self.name}")

    def brand_phrase(self):
        print('Радианты всегда одерживают победу!!!!!!!!!!')

h1=Hero('Бакай','danxhopa',100,500)
h2=Hero('Эльдар','Mxqnn',500,1000)
h3=Hero('Дидар','happydieyoung',5,10)
h4=Hero('Мирай','miraika',1,0)

h1.two_damage()
h2.heal()
h3.gritting()
h4.brand_phrase()

