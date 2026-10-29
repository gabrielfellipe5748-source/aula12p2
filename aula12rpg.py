import random


mapa_tiles = [
    'BBBBBBBBBBBBBBBBBBBB',
    'B..................B',
    'B.....E............B',
    'B............B.....B',
    'B..BBBBB.....B.....B',
    'B...B........B.....B',
    'B...B..............B',
    'B...B.......BBB....B',
    'B..................B',
    'B.....BBBB.........B',
    'B.......E..........B',
    'B.............P....B',
    'B..................B',
    'B.....E............B',
    'BBBBBBBBBBBBBBBBBBBB',
]


ICONE_JOGADOR = '@'  #Ou sinta-se à vontade para escolher outro ícone :D

class Mundo:
    def __init__(self):
        self.grade = [list(linha) for linha in mapa_tiles] #Preencha com o for de uma linha só
        self.jogador_x = 0
        self.jogador_y = 0
        self.inimigos = [] 


        for y, linha in enumerate(self.grade): #Preencha para obter o valor y e o valor da linha
            for x, celula in enumerate(linha):  #Preencha para obter o valor de x e da celular
                if celula == 'P':
                    self.jogador_x, self.jogador_y = x, y
                    self.grade[y][x] = '.'
                elif celula == 'E':
                    self.inimigos.append([x, y])
                    self.grade[y][x] = '.'
                    
    def mover_jogador(self, dx, dy):
        novo_x = self.jogador_x + dx
        novo_y = self.jogador_y + dy
        self.jogador_x, self.jogador_y = novo_x, novo_y
    def inimigo_em(self, x, y):
        for inimigo in self.inimigos:
            if inimigo[0] == x and inimigo[1] == y:
                return inimigo
        return None
    def renderizar(self):
        for y, linha in enumerate(self.grade):
            texto_linha = ""
            for x, celula in enumerate(linha):
                if (x, y) == (self.jogador_x, self.jogador_y): #If para detecção do player
                    texto_linha += "@"  #Se achar o Player, o que ele tem que renderizar?
                elif self.inimigo_em(x, y):  #elif para detectar o inimigo
                    texto_linha += "E" #Se achar um inimigo, o que tem que renderizar?
                else:
                    texto_linha += celula # E se não achar nada? O que tem que renderizar?
            print("|" + texto_linha + "|") #Aqui será printado a linha toda. 
        print("Movimento: W (cima) / S (baixo) / A (esquerda) / D (direita) / Q (sair)") #Spoiler da movimentação :D 

def executar():
    mundo = Mundo()         # Crie aqui o objeto mundo
    rodando = True     


    while rodando:          # Colocando o projeto para rodar
        mundo.renderizar()  # Renderiza o projeto
        comando = input("\n> ").strip().lower()    


        if comando == 'w':              # Comando para andar pra cima
            mundo.mover_jogador(0, -1)
        elif comando == "s":            # Andar para baixo. O que precisa mudar?
            mundo.mover_jogador(0, 1) # E aqui?
        elif comando == "a":           # E para a esquerda?
            mundo.mover_jogador(-1, 0)
        elif comando == "d":           # E para a direita?
            mundo.mover_jogador(1, 0) 
        elif comando == 'q':            # Q para quitar do jogo
            rodando = False
            continue
        else:
            print("Comando inválido.")
            continue


    print("Obrigado por jogar!")


executar()
