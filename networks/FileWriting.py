'''
@author Fabiana Barreto Pereira
'''

import math


class FileWriting:
    '''
    Método escreve em um arquivo externo p(k) x k em uma rede WS
    '''
    def write_grades_ocur(self, degree, players, neighbor_ini, prob, sample):
        nome = "k x ocorrencias -{} amostra {} vizinhos e {} jogadores.dat".format(sample, neighbor_ini, players)
        file = open(str(nome), 'a')
        fist_line = "# k x ocorrências - prob= {}\n".format(prob)
        file.write(str(fist_line))
        file.write("\n")
        for i in range(players):
            if degree[i] > 0:
                file.write(str(i))
                file.write(" ")
                file.write(str(degree[i]))
                file.write("\n")
        file.write("\n")
        file.write("\n")
        file.flush()
        file.close()


    '''
    Método escreve em um arquivo externo a rede quadrada resultante 
    '''
    def write_square(self,lattice,side):
        nome ="Rede -{}x{}.dat".format(side,side)
        file=open(str(nome),'a')
        for i in range(len(lattice)):
            for j in range(len(lattice[i])):
                file.write(str(i))
                file.write("  ")
                file.write(str(lattice[i][j]))
                file.write("\n")
                file.write("\n")

        file.flush()
        file.close()
