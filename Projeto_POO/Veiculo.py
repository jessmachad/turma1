class Veiculo:
    def dirigir(self):
        return "O veículo está em movimento"

    def descricao(self):
        return f"{self.__class__.__name__}: {self.dirigir()}"


class Carro(Veiculo):
    def dirigir(self):
        return "O carro está em movimento"


class Moto(Veiculo):
    def dirigir(self):
        return "A moto está acelerando"


class Caminhao(Veiculo):
    def dirigir(self):
        return "O caminhão está na estrada"


# Programa principal
veiculos = [Carro(), Moto(), Caminhao()]

for v in veiculos:

    print(v.descricao())


# teste mudança

# testando jms
