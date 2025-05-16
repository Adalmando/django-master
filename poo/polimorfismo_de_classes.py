class Animal:

    def emitir_som(self):
        print("Qualquer som...")

class Cachorro(Animal):
    
    # Aqui eu sobrescrevi a função emitir som que foi Herdada de Animal, mas so mudei o resultado dela na classe Cachorro (polimorfismo)
    def emitir_som(self):
        print("Au au!")    

class Gato(Animal):
    
    # Aqui eu sobrescrevi a função emitir som que foi Herdada de Animal, mas so mudei o resultado dela na classe Gato (polimorfismo)
    def emitir_som(self):
        print("Miau!")    

class Rato(Animal):
    
    # Observe que na classe Rato eu nao sobrescrevi a função emitir som que foi herdada de Animal, logo ela vai retornar o valor padrão (sem polimorfismo) 
    ...

cachorro = Cachorro()
cachorro.emitir_som()

gato = Gato()
gato.emitir_som()

rato = Rato()
rato.emitir_som()