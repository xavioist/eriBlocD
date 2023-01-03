# Exercici 1
""" Genera una llista de 876 nombres enters fent servir la funció linspace de numpy
"""

# Exercici 2
""" Fent servir numpy, importa el contingut del fitxer dades.csv. Fes servir la funció 
genfromtxt("NOM_ARXIU", delimiter=","). Separa el seu contingut en dues variables, una per les dades de
la primera columna i l'altra per les dades de la segona.

PISTA: L'arxiu un cop carregat es comportarà com una matriu n x m. Per accedir
als seus continguts, pots fer matriu[0][0], matriu[0][1] i veure què dona.
Si salta l'error IndexError vol dir que li estàs demanant elements que no té.

SOLUCIÓ:
import numpy as np

foo = np.genfromtxt("dades.csv", delimiter=",", dtype=float)

x = [foo[i][0] for i in range(len(foo))]

y = [foo[i][1] for i in range(len(foo))]

"""

# Exercici 3
""" Fes servir els resultats de l'exercici 2 i grafica'ls amb matplotlib.
Importa matplotlib fent (import matplotlib.pyplot as plt) i fes servir la funció plot.

Alternativament, genera amb numpy dos arrays amb valors aleatoris i fes-ne la
gràfica.
"""

# Exercici 4
""" Fes un array en 2D amb numpy (una matriu 3x3)

PISTA: https://www.w3schools.com/python/numpy/numpy_creating_arrays.asp
"""

# Exercici 5
""" Fes una gràfica partint dels valors:

x_val = [1,2,3,4,5,6,7,8,9,10]
y_val = [2,4,6,8,10,12,14,16,18,20]

i que tingui títols als eixos de les X (eix X) i de les de Y (eix Y).
Juga amb el tipus de gràfic que pots fer, explorant les opcions de plt.plot

(mira l'argument "linestyle" de plt.plot
PISTA: https://www.w3schools.com/python/matplotlib_line.asp)
"""

# Exercici 6

""" Amb els valors donats a l'exercici 5 i amb aquest:

z_val = [3,6,9,12,15,18,21,24,27,30]

fes una gràfica amb un subplot que contingui les dues gràfiques i títols als eixos.
Juga amb el tipus de gràfic que pots fer.

PISTA: https://www.w3schools.com/python/matplotlib_subplot.asp
"""
