'''
@author Fabiana Barreto Pereira
'''
import numpy as np


'''
Método para gerar uma semente pseudoaleatória diferente para cada amostra
@param número da amostra (>=1)
'''
def roulette(nspin):
    np.random.seed(2500)
    for i in range(nspin):
        seed=np.random.random()*65539
    return int(seed)
