'''
@author Fabiana Barreto Pereira
'''

'''
Código para criar diferentes tipos de redes (quadrada, regular, e Watts e Strogatz)
'''

import math
import numpy as np
import ControlRandom as cr
import FileWriting as FW


#lattice: Lista de listas. Seja N jogadores (i=0,i=1,...,i=N-1), cada elemento i da lista principal corresponde a uma lista dos vizinhos do jogador i.
global lattice
lattice= list()

'''
classe para criar uma rede quadrada de 4 vizinhos e n_side lados
'''
class Square:
    '''
    Contrutor
    @param número de lados da rede
    '''
    def __init__(self,n_side):
        self._n_side=n_side
        self._nodes=n_side*n_side

    '''
    Método para construir a rede
    @return uma rede quadrada
    '''
    def filllatice(self):
        #adicionando vértices, jogadores
        global lattice
        lattice=[[] for j in range(self._nodes)]

        #adicionando vizinhos
        col1=0
        coln=self._n_side-1
        lin1=self._n_side-1
        linn=self._nodes-self._n_side

        for i in range(self._nodes):
            if (i%self._n_side)==0 and i>0:
                col1+=self._n_side
            if ((i+1)%self._n_side)==0 and i>(self._n_side-1):
                coln+=self._n_side

            #1a coluna
            if i==col1 and i>lin1 and i<linn:
                lattice[i].append(i+self._n_side)
                lattice[i].append(i-self._n_side)
                lattice[i].append(i+(self._n_side-1))
                lattice[i].append(i+1)
            #última coluna
            elif i==coln and i>lin1 and i<linn:
                lattice[i].append(i+self._n_side)
                lattice[i].append(i-self._n_side)
                lattice[i].append(i-1)
                lattice[i].append(i-(self._n_side-1))
            #miolo
            elif i!=col1 and i!=coln and i>lin1 and i<linn:
                lattice[i].append(i+self._n_side)
                lattice[i].append(i-self._n_side)
                lattice[i].append(i-1)
                lattice[i].append(i+1)

            #primeira linha
            elif i>0 and i<lin1:
                lattice[i].append(i+self._n_side)
                lattice[i].append(i+(self._nodes-self._n_side))
                lattice[i].append(i-1)
                lattice[i].append(i+1)
            #última linha
            elif i>linn and i<(self._nodes-1):
                lattice[i].append(i-self._n_side)
                lattice[i].append(i-(self._nodes-self._n_side))
                lattice[i].append(i-1)
                lattice[i].append(i+1)
            #pontas
            elif i==0:
                lattice[i].append(1)
                lattice[i].append(self._n_side-1)
                lattice[i].append(self._n_side)
                lattice[i].append(self._nodes-self._n_side)
            elif i==(self._n_side-1):
                lattice[i].append(self._nodes-1)
                lattice[i].append(0)
                lattice[i].append(i-1)
                lattice[i].append(i+self._n_side)
            elif i==(self._nodes-self._n_side):
                lattice[i].append(0)
                lattice[i].append(i-self._n_side)
                lattice[i].append(self._nodes-1)
                lattice[i].append(i+1)
            elif i==(self._nodes-1):
                lattice[i].append(self._n_side-1)
                lattice[i].append(i-self._n_side)
                lattice[i].append(i-1)
                lattice[i].append(self._nodes-self._n_side)

        fw = FW.FileWriting()
        fw.write_square(lattice,self._n_side)
        return lattice



'''
Classe para contruir uma rede regular de n_players jogadores e n_neighbors vizinhos
'''
class Onidimensional:
    '''
    Construtor
    @param número de jogadores
    @param número de vizinhos
    '''
    def __init__(self,n_players,n_neighbors): #construtor
        self.__nPlayers=n_players
        self.__nNeighbors=n_neighbors

    '''
    Método para construir a rede
    @return uma rede regular unidimensional
    '''
    def filllatice(self):
        # adicionando vértices, jogadores
        global lattice
        lattice=[[] for j in range(self.__nPlayers)] #lista de lista, cada lista interna será a lista de vizinhos

        # adicionando vizinhos
        # vizinhos da esquerda
        tam = self.__nNeighbors - int(self.__nNeighbors / 2)
        for i in range(tam):
            for j in range(self.__nPlayers):
                #calculando vizinho
                aux = int(i + j + 1)
                aux = aux % self.__nPlayers
                #adicionando o vizinho na lista do jogador
                lattice[j].append(aux)

        # vizinhos da direita
        tam = int(self.__nNeighbors / 2)
        for i in range(tam):
            for j in range(self.__nPlayers):
                # calculando vizinho
                aux = int(j + self.__nPlayers - i - 1)
                aux = aux % self.__nPlayers
                # adicionando o vizinho na lista do jogador
                lattice[j].append(aux)

        return lattice


'''
Classe para construir uma rede Watts e Strogatz de n_players jogadores, n_neighbors_ini vizinhos iniciais, probabilidade de redistribuição de links prob, e semente idum.
'''
class WS:
    '''
    Construtor
    @param número de jogadores
    @param número de vizinhos iniciais
    @param probabilidade de redistribuição de links
    @param semente
    '''
    def __init__(self,n_players,n_neighbors_ini,prob,idum):
        self.__nPlayers=n_players
        self.__nNeigborsIni=n_neighbors_ini
        self.__prob=prob
        self.__degree=[0 for i in(range(n_players))]
        self.__idum=idum
        np.random.seed(self.__idum)

    '''
    Método para contruir a rede inicial
    @return uma rede inicial
    '''
    def filllatice(self):

        #lattice.clear()
        # adicionando vértices, jogadores
        global lattice
        lattice=[[] for j in range(self.__nPlayers)] #lista de lista, cada lista interna será a lista de vizinhos

        # adicionando vizinhos
        # vizinhos da esquerda
        tam = self.__nNeigborsIni - int(self.__nNeigborsIni / 2)
        for i in range(tam):
            for j in range(self.__nPlayers):
                # calculando vizinho
                aux = int(i + j + 1)
                aux = aux % self.__nPlayers
                # adicionando o vizinho na lista do jogador
                lattice[j].append(aux)

        # vizinhos da direita
        tam = int(self.__nNeigborsIni / 2)
        for i in range(tam):
            for j in range(self.__nPlayers):
                # calculando vizinho
                aux = int(j + self.__nPlayers - i - 1)
                aux = aux % self.__nPlayers
                # adicionando o vizinho na lista do jogador
                lattice[j].append(aux)

        return lattice

    '''
    Método para fazer reconexões de links
    @return uma rede Watts e Strogatz
    '''
    def reconnectionlattice(self):
        player=0
        chosen=0
        neighbor=0
        global lattice
        if self.__prob!=0: #probabilidade 0 não mexe no código
            for i in range(int(self.__nNeigborsIni/2)):
                for j in range(self.__nPlayers):
                    player=j
                    chosen=(np.random.randint(0,self.__nPlayers)) #escolher um jogador em toda rede

                    if(j!=chosen) and (j not in lattice[chosen]): #se existe aresta
                        neighbor=lattice[j][i]

                        if neighbor <0:
                            break
                        data= np.random.random()
                        if self.__prob>=data:
                            # colocar -1 o vizinho do jogador
                            lattice[player][i]=-1
                            #colocar - 1 o jogador na vzinhança do vizinho
                            for q in range(len(lattice[neighbor])):
                                if lattice[neighbor][q]==player:
                                    lattice[neighbor][q]=-1
                                    break
                            # atualizando vizinhos (colocando aresta)
                            lattice[player].append(chosen)
                            lattice[chosen].append(player)
        # Tirando os nós removidos (-1)
        for h in range(self.__nPlayers):
            u=0
            while u<len(lattice[h]):
                if lattice[h][u]==-1:
                    lattice[h].pop(u)
                    u-=1

                u+=1
        cont=0

        #verificando grau dos vértices
        for a in lattice:
            cont=len(a)
            self.__degree[cont]=self.__degree[cont]+1

        return lattice

    '''
    Método para computar a probabilidade de encontrar cada k vizinhos (p(k) x k)
    @param número de amostras
    @param probabilidade de redirecionamento de links
    '''
    def control(self,sample,prob):
        self.__degree=[0 for j in range(self.__nPlayers)]
        self.__prob=prob

        for j in range(0,sample):
            a=j+1
            _seed=cr.roulette(a)
            np.random.seed(_seed)
            self.filllatice()
            self.reconnectionlattice()

        #computa a média
        for j in range(0, len(self.__degree)):
            self.__degree[j]=float(self.__degree[j] / sample);
            self.__degree[j] = float(self.__degree[j] / self.__nPlayers)
            if self.__degree[j] < float( 1/ self.__nPlayers):
                self.__degree[j]=0

        fw = FW.FileWriting()
        fw.write_grades_ocur(self.__degree,self.__nPlayers,self.__nNeigborsIni,self.__prob,sample) #escreve relação p(k) x k em um arquivo externo




if __name__=="__main__":
    s=WS(1000,5,0.01,3)
    s.control(10000,0.01)
