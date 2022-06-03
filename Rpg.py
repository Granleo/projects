import keyboard
import random


class Classes:

    def __init__(self, nome, hab):
        self.nome = nome
        self.hab = hab

    def shab(self):
        if self == 1:
            if Personagem.classes == 'Mago':
                Classes.hab = ['mhab1, mhab2, mhab3']
                return Classes.hab
            elif Personagem.classes == 'Guerreiro':
                Classes.hab = ['ghab1, ghab2, ghab3']
                return Classes.hab
            else:
                Classes.hab = ['ahab1, ahab2, ahab3']
                return Classes.hab


class Personagem:
    atributos = None
    classes = None
    lista_classes = ['Arqueiro', 'Mago', 'Guerreiro']

    def __init__(self, nome, classes, atributos, vida, energia):
        self.nome = nome
        self.classes = classes
        self.atributo = atributos
        self.vida = vida
        Personagem.vida = ((atributos[0] / 2) - 10) * 100
        self.energia = energia
        Personagem.energia = ((atributos[1] / 2) - 10) * 100

    def snome(self):
        if self == 1:
            Personagem.nome = str(input('Qual o nome do personagem?'))
            return Personagem.nome

    def sclasse(self):
        while self == 1:
            lista_classes = ['Arqueiro', 'Mago', 'Guerreiro']
            Personagem.classes = str(input('Pick a class: \n%s \n' % lista_classes))
            if lista_classes.count(Personagem.classes) == 0:
                print('Classe inválida')
            else:
                '''print(Personagem.classes)'''
                return Personagem.classes

    def satrb(self):
        if self == 1:
            '''print('Seus atributos serão: ')
          lista_atrb = ['Corpo', 'Mente', 'Destreza', 'Carisma']'''
            Personagem.atributos = []
            for x in range(4):
                dice = random.randrange(9, 19)
                Personagem.atributos.append(dice)
                '''print('%s %s' % (lista_atrb.__getitem__(x), dice))'''
            return Personagem.atributos

    def svida(self):
        if self == 1:
            Personagem.vida = ((Personagem.atributos[0] / 2) + 10) * 100
            return Personagem.vida

    def senergia(self):
        if self == 1:
            Personagem.energia = ((Personagem.atributos[1] / 2) + 10) * 100
            return Personagem.energia


class Inimigos(Personagem):

    def __init__(self, nome, classes, atributos, vida, energia):
        super().__init__(nome, classes, atributos, vida, energia)

    def snome(self):
        if self == 1:
            lista_ini = ['Iuz o Maligno', 'Asmodeus', 'Lolth', 'Kas']
            Inimigos.nome = lista_ini[random.randrange(0, 3)]

    def sclasse(self):
        if self == 1:
            lista_classes = ['Arqueiro', 'Mago', 'Guerreiro']
            Inimigos.classes = lista_classes[random.randrange(0, 2)]


def perclasse():
    Personagem.sclasse(1)
    perClasse = Classes(Personagem.classes, Classes.shab(1))
    return perClasse


# vvv Programa vvv

ini = Inimigos(Inimigos.snome(1), Inimigos.sclasse(1), Inimigos.satrb(1),
               Inimigos.svida(1), Inimigos.senergia(1))

print('Press Enter to start')
while True:
    if keyboard.is_pressed('Enter'):
        a = input()

        per = Personagem(Personagem.snome(1), perclasse(), Personagem.satrb(1),
                         Personagem.svida(1), Personagem.senergia(1))

        if per.classes == 'Mago':
            per.atributo[1] += 2
            per.atributo[0] -= 2
        elif per.classes == 'Guerreiro':
            per.atributo[3] -= 2
            per.atributo[0] += 1
            per.atributo[2] += 1
        elif per.classes == 'Arqueiro':
            per.atributo[0] -= 1
            per.atributo[2] += 2
            per.atributo[3] -= 1

        print()
        print('Player')
        print(per.nome, Personagem.classes, '\nAtributos: \n [Corpo, Mente, Destreza, Carisma]\n', per.atributo,
              '\n\nVida:', per.vida, '\nMana:', per.energia)
        print()
        print('Inimigo')
        print(Inimigos.nome, Inimigos.classes, '\nAtributos: \n [Corpo, Mente, Destreza, Carisma]\n', ini.atributo,
              '\n\nVida:', ini.vida, '\nMana:', ini.energia)
