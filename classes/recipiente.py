class Recipiente:
    def __init__(self, tamanho=0, conteudo: float=0, limpo=True):
        if(tamanho < 0):
            self.tamanho = 0
        else:
            self.tamanho = tamanho
        self.conteudo = conteudo
        self.limpo = limpo
    
    def esvaziar(self):
        self.conteudo = 0
    
    def esta_vazio(self):
        if(self.conteudo <= 0):
            return True
        return False

    def lavar(self): 
        self.conteudo = 0
        self.limpo = True
    
    def esta_limpo(self):
        if(self.limpo == True):
            return True
        return False

    def estado(self):
        if(self.limpo == True):
            return "limpo"
        return "sujo"

    def sujar(self):
        self.limpo = False

    def __str__(self):
        return f'Um recipiente {self.estado()} não especificado'
    
    def __repr__(self):
        return f'Um recipiente {self.estado()} não especificado'