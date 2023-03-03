# Exercici 0
"""  La funció standard de python print() és enormement útil en qualsevol context
de programació. Ens permet imprimir per pantalla el valor d'una variable (monitorització),
seguir l'execució d'un programa amb missatges de checkpoint o historials,
ens ajuda a arreglar un programa quan hi ha errors, etc. Pren-te un temps per a familiaritzar-te
amb la funció print().

print() imprimeix variables i text: tot el text va entre cometes i les variables
van excrites tal qual, separades del text que volguem escriure per comes.

i.e: 
var = 33
print(var, "és un nombre curiós!")

"""

# Exercici 1

"""Fes un petit programa on defineixis unes variables X i Y (poden ser qualsevol cosa)
i juga amb blocs condicionals "if" per a veure com es comporten. i.e: Fes servir els operadors <, 
>, >=... etc conjuntament amb els operadors booleans "and", "or"... que hem vist a classe.
També pots incloure varis blocs condicionals if, elif i else. Comprova les diferències
de fer servir varis "if" seguits vs utilitzar "if" i "elif".

i.e:

X = 42
Y = 15

if X>Y and X/2 >= Y:
    X *=2
    if X > 100:
        print(X, "es mes gran que 100")
    elif X > 4*Y:
        print(X, "es mes gran que 4 vegades Y")
    else:
        print("cap condicional anterior es cumpleix")
    
"""
# Exercici 2

"""  Fes servir un bucle for per iterar sobre una llista de la teva elecció.
Recorda que en python, la sintaxi per iterar acostuma a ser força literal

i.e: per cada element dins la llista -> es tradueix a;
for element in list:

donada la llista llista = [1,2,3,4,"cinc",6] fes un loop que imprimeixi cada element
de la llista
"""

# Exercici 3
""" La funció standard de python len() ens permet veure quants objectes conté una llista.
Fes servir la funció len() per iterar sobre una llista i que imprimeixi per pantalla
cada element.

PISTA: recorda que els elements d'una llista es poden accedir mitjançant un índex enter.
llista = [1,2,3,4,"cinc"] -> llista[4] = "cinc"
"""

# Exercici 3.1
"""  El "slicing" és una manera d'agafar determinats valors d'una llista de python.
La seva sintaxi és my_list[inici:final:increment]. Es compta l'inici, però no
el final. 

documentació: https://www.geeksforgeeks.org/python-list-slicing/

i.e: mylist = [1,2,3,4,5,6,7,8,9]
newlist = mylist[2:4] -> [3,4]
newlist2 = mylist[:7:2] -> [1,3,5,7] (pots deixar índexs en blanc)
newlist3 = mylist[1:-3] -> [2,3,4,5,6] (també compta amb índex negatius)

myword = "abcdefghijk"
new_word = myword[3:8] -> "defgh"
"""

# Exercici 4
""" La funció standard de python range() ens permet obtenir un rang de nombres separats
per un interaval fix. Comprova com funciona la funció range() fent-la servir dins un bucle
for i  imprimint els resultats per pantalla amb la funció print(). 

"""

# Exercici 5
""" Els comptadors són un tipus de variable molt útil quan volem comptar els cops que
passa quelcom. Acostumen a fer-se servir conjuntament amb blocs for. Fes un programa que
tingui una variable counter = 0 i un bucle for que s'executi 100 vegades. Cada cop que el
bucle for dóna un múltiple de 5, suma una unitat al comptador. 

RECORDA: Per a saber si un nombre és múltiple d'un altre fem servir la funció
mòdul (%). És important el moment del bucle for en el que actualitzem el valor del 
comptador. Comprova que si canviem el moment on actualitzem la variable counter
podem alterar el funcionament del programa.

i.e: 
counter = 0
for n in (...):
    if n % 5 == 0:
        
"""

# Exercici 6
""" Fes una funció o un petit programa que, donada una paraula, et digui
quantes lletres té per pantalla.

"""

# Exercici 7
""" Els diccionaris són també molt útils com a estructures de dades, ja que ens donen
accès als seus valors utilitzant una keyword. Fes un diccionari que contingui parells
de clau:valor qualsevols i familiaritza't amb la seva sintaxi i com accedir als valors.

i.e: my_dict = {"Albània":4.3, "Algèria":8.9, "Zimbabwe":5.5}
my_dict["Zimbabwe"] -> 5.5

comprova que pots iterar sobre els elements d'un diccionari fent servir:

for item, keys in my_dict:
    print(item, keys)
"""

# Exercici 8
""" Escriu en un paper (o en un document de text) el pseudocodi d'un programa
que, agafant els teus gastos mensuals d'un full d'excel, et digui, segons uns valors
límit, en quin(s) àmbit(s) podries estalviar.

i.e: el excel està repartit en:

Oci : 143$
Menjar: 289 $
Transport: 150$
Roba: 70$
...

i el programa agafa cada categoria i segons un criteri (que decideixes tu) et diu
si has gastat més del compte o no.
"""

# Exercici 9
""" Agafant el pseudocodi de l'exercici 7 i un diccionari com a element d'entrada, transforma-ho en
un programa de python.

i.e:

gastos = {"oci":143, "menjar":289, ...}
"""
