from pygame import mixer
import time

mixer.init()
mixer.music.load("carro_ligando.mp3")


class Carro:
    def __init__(self, potencia, velocidade_maxima):
        self.velocidade_atual = 0
        self.potencia = potencia
        self.velocidade_maxima = velocidade_maxima
        self.ligado = False

    def ligar(self):
        self.ligado = True
        mixer.music.play()
        time.sleep(1.75)

    def acelerar(self):
        if self.ligado == False:
            print('Seu carro está desligado!!!')
        else:
            if self.velocidade_maxima - self.velocidade_atual < self.potencia:
                self.velocidade_atual = self.velocidade_maxima
                print('Seu carro está na velocidade maxima!!!')
            else:
                self.velocidade_atual += self.potencia

    def freiar(self, segundos):
        if self.ligado == False:
            print('Seu carro está desligado!!!')
        else:
            segundos *= int(self.potencia / 2)
            self.velocidade_atual -= segundos


Ferrari = Carro(20, 200)
Ferrari.acelerar()
Ferrari.freiar(1)
Ferrari.ligar()
while Ferrari.velocidade_atual < Ferrari.velocidade_maxima:
    Ferrari.acelerar()
    print(f'VRUUM... VRUMM... velocidade atual: {Ferrari.velocidade_atual}')

Ferrari.freiar(1)
print(f'shiiiiii!!! velocidade atual: {Ferrari.velocidade_atual}')