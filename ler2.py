import struct
from datetime import datetime

class dados():
    def __init__(self, nome:str, nasc:str, genero:str, peso:float, altura:float):
        self.nome = nome
        self.nasc = nasc
        self.genero = genero
        self.peso = peso
        self.altura = altura

    def calcIdade(self):
        n = datetime.strptime(self.nasc, "%Y-%m-%d")
        return (datetime.now() - n).days // 365

    def getTarget(self):
        idade = self.calcIdade()
        imc = self.peso / (self.altura**2)
        
        if idade < 6 or idade > 8:
            raise ValueError("Idade fora da faixa permitida (6-8 anos)")
        
        if self.genero == 'Masc':
            if idade == 6:
                if imc < 14.5: return 0
                elif 14.5 <= imc < 16.7: return 1
                elif 16.7 <= imc < 18: return 2
                else: return 3
            elif idade == 7:
                if imc < 15: return 0
                elif 15 <= imc < 17.4: return 1
                elif 17.4 <= imc < 19.1: return 2
                else: return 3
            elif idade == 8:
                if imc < 15.6: return 0
                elif 15.6 <= imc < 16.8: return 1
                elif 16.8 <= imc < 20.3: return 2
                else: return 3
        elif self.genero == 'Femi':
            if idade == 6:
                if imc < 14.3: return 0
                elif 14.3 <= imc < 16.2: return 1
                elif 16.2 <= imc < 17.4: return 2
                else: return 3
            elif idade == 7:
                if imc < 14.9: return 0
                elif 14.9 <= imc < 17.2: return 1
                elif 17.2 <= imc < 18.9: return 2
                else: return 3
            elif idade == 8:
                if imc < 15.6: return 0
                elif 15.6 <= imc < 17.3: return 1
                elif 17.3 <= imc < 20.3: return 2
                else: return 3
        else:
            raise ValueError("Gênero inválido. Use 'Masc' ou 'Femi'")

    def __str__(self) -> str:
        return (f"Nome: {self.nome}\n"
                f"Data de Nascimento: {self.nasc}\n"
                f"Gênero: {self.genero}\n"
                f"Idade: {self.calcIdade()}\n"
                f"Peso: {self.peso} Kg\n"
                f"Altura: {self.altura} m\n"
                f"Interpretação IMC: {self.getTarget()}")

def ler_dados(arq):
    form = '30s 11s 4s f f i'
    tam = struct.calcsize(form)

    with open(arq, 'rb') as f:
        while True:
            record_data = f.read(tam)
            if not record_data:
                break
            record = struct.unpack(form, record_data)
            string1 = record[0].decode().strip('\x00')
            string2 = record[1].decode().strip('\x00')
            string3 = record[2].decode().strip('\x00')
            float1 = record[3]
            float2 = record[4]
            integer = record[5]
            dado = dados(string1, string2, string3, float1, float2)
            print(dado)

if __name__ == '__main__':
    ler_dados('dados.bin')