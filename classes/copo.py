from classes.recipiente import Recipiente

class Copo(Recipiente):
    def __init__(self, tamanho):
        super().__init__(tamanho)
        self.tamanho = tamanho
    
    def encher(self, bebida = 'água'):
        if(self.limpo == False):
            return 'Não se pode encher um copo sujo'
        self.limpo = False
        self.bebida = bebida
        self.conteudo = self.tamanho
    
    def beber(self, quantidade):
        if(quantidade < 0):
            return 'Quantidade deve ser positiva'
        elif(quantidade > self.conteudo):
            return 'Não há bebida suficiente no copo'
        else:
            self.conteudo = self.conteudo - quantidade
    
    def lavar(self):
        self.bebida = None
        self.conteudo = 0
        self.limpo = True

    def __str__(self):
        if(self.conteudo <= 0):
            return f'Um copo vazio de {float(self.tamanho)}ml'
        return f'Um copo de {float(self.tamanho)}ml contendo {float(self.conteudo)}ml de {self.bebida}'
    
    def __repr__(self):
        if(self.conteudo <= 0):
            return f'Um copo vazio de {float(self.tamanho)}ml'
        return f'Um copo de {float(self.tamanho)}ml contendo {float(self.conteudo)}ml de {self.bebida}'