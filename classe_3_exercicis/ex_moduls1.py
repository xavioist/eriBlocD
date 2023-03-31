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

Amb slicing:

foo = np.genfromtxt("dades.csv", delimiter=",", dtype=float)

x = foo[:, 0]
y = foo[:, 1]

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

# Exercici 7

""" Pandas té els DataFrames, que són estructures de dades molt potents per a manipular arxius csv i similars.
En un arxiu csv a vegades hi ha un "header", una línea inicial d'informació que només aporta context i no compta com a dades.
Els headers són útils per nosaltres perquè ens diuen quin tipus de dades estem tractant (mireu, per exemple, la primera fila del deniro.csv on ens
dona informació sobre el tipus de dades de cada columna). Feu servir pandas per a carregar l'arxiu deniro.csv i convertir-lo en un dataframe
sense tenir en compte el header amb read_csv(). Un cop carregat, ordeneu les entrades del dataframe segons l'any (mètode sort_values() dels
dataframes de pandas)

COMPTE! Alguns csv poden donar problemes ja que no estan ben formatats. Per sort, pandas ens
proporciona moltes maneres de, sense alterar el csv, poder-lo carregar corrctament. Doneu un cop d'ull a l'argument "usecols" de read_csv().
"""

# Exercici 8

""" Pandas també et permet fer servir Series, una estructura de dades que converteix les llistes en arrays uni-dimensionals indexats.
És més fàcil veure què són amb un exemple: donades la string i la llista str = 'abcdefgh' num = [1,2,3,4,5,6,7,8] convertiu-les cadascuna a una sèrie de pandas.
fent servir la funció Series. PISTA: Comenceu per la llista num. 
Per a "str", heu d'obtenir un resultat similar: teniu una string i l'heu de convertir a llista per a que la sèrie ho entengui.
"""


# Exercici 9

""" https://pandas.pydata.org/docs/reference/api/pandas.Series.html#
"""
