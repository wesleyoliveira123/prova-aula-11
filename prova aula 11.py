class Animal:
    def Falar(self):
        return f"Este animal faz um som."

class Cachorro(Animal):
    def Latir(self):
        return f"O cachorro late."

class Gato(Animal):
    def Miar(self):
        return f"O gato mia."


animal=Animal()
cachorro=Cachorro()
gato=Gato()

print(animal.Falar())
print(cachorro.Latir())
print(gato.Miar())
