# Problema amb numpy, plt i d'altres

# Exercici 1
""" L'arxiu nile.csv conté una llista de 570 anys i el nivell de l'aigua del riu Nil
aquell any. Carrega aquestes dades des del csv, però queda't només els anys que tinguin
un nivell d'aigua superior a 12.3 metres cúbics. També has de tenir en compte
que l'arxiu té una capcelera que has d'ometre sense modificar l'arxiu.
Tot seguit, fes un gràfic de barres en matplotlib, títols als eixos
de les X (anys) i de les Y (volum aigua (m^3)) i amb el títol "Crescudes del riu Nil".
"""
# Solució:

import numpy as np
import matplotlib.pyplot as plt

# carreguem el csv, amb skip_header per a no comptar la primera línea
# generem un comptador i una llista per a guardar els índexs que ens interessen
data = np.genfromtxt("nile.csv", delimiter=",", skip_header=True)
pos = 0
index = []

for element in data[:, 1]:
    """Si els elements de la columna 1 (volum aigua)
    són majors a 10.3, guarda la seva posició en un array.
    """
    if element > 12.3:
        pos += 1
    else:
        index.append(pos)
        pos += 1

# borra els elements de l'array que estiguin a la posició
# index. Axis=0 ens diu que borrem les files. Definim noves variables
# amb les dades que volem
new_data = np.delete(data, index, axis=0)
years = new_data[:, 0]
water = new_data[:, 1]

plt.bar(years, water, width=5)
plt.xlabel("Anys de crescudes")
plt.ylabel("Volum aigua (m^3)")
plt.title("Crescudes del riu Nil")
plt.show()
