class Carro:
    numero_rodas = 4
    quantidade_passageiros = 5 

    def acelerar(self):
        print("Acelerando...")

    def frear(self):
        print("Freando...")
    
    def buzinar(self):
        print("Buzinando...")

carro1 = Carro()
carro1.acelerar()

# Classe Uno herda classe Carro, ou seja, todos os parametros e metodos de Carro podem ser usados em Uno
class Uno(Carro):
    modelo = "Uno"
    marca = "Fiat"
    ano = 2010

# Observe que com a heranca de Carro, Uno pode usar os mesmos atributos e métodos de Carro
carro2 = Uno()
print(carro2.modelo)
carro2.acelerar()
print(carro2.quantidade_passageiros)