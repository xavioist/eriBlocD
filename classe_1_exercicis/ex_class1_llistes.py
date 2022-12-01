"""Introducció a llistes

Les llistes són una estructura de dades molt útil per a emmagatzemar informació
i poder utilitzar-la i accedir a ella de manera controlada. Són mutables
(els seus elements poden canviar), permeten emmagatzemar tot tipus d'elements
i són iterables (es pot fer un loop sobre els seus elements). A més, admeten
operacions amb operadors algebraics com (*) (la multiplicació, que sobre llistes
actua com a concatenador).

i.e: n = 3

    llista = [True]* n 
    print(llista)
    
    #resultat: [True, True, True]
    
Les llistes també estan indexades, el que significa que cada element de la llista té
associada una posició. En python, les llistes comencen en 0, i per accedir a elements 
concrets fem servir la següent sintaxi:

i.e: lst = ['primer', 'segon', 'tercer']
    print(lst[0])  #resultat: 'primer'
    print(lst[1])  #resultat: 'segon'
    print(lst[2])  #resultat: 'tercer'
    
    #si li demanem un índex que no existeix:
    
    print(lst[3])  #resultat: "IndexError: list index out of range"


Per iniciar-les es pot fer una "list comprehension", que té una sintaxi més
intuitiva o bé anar afegint valors des d'un bucle for o while. També es poden fer
llistes buides i anar-les omplint amb els valors que vulguem.

i.e: empty_list = [] #llista buida

    list_2 = [x for x in range(1, 42)]
    
    list_2 = []
    for x in range(1, 42):
        list_2.append(x)


Les llistes també tenen tot un seguit de funcions bàsiques que se'ls poden aplicar
pel sol fet de ser llistes. Aquestes funcions (també anomenades mètodes) les trobareu a 

    https://www.w3schools.com/python/python_ref_list.asp

Les aplicarem mitjançant l'operador punt (.) sobre una llista definida.

i.e: llista_2 = []

    print(llista_2)  #resultat: []
    
    llista_2.append(4)
    llista_2.append('hola')
    
    print(llista_2) #resultat [4, 'hola']
    
    llista_2.pop(0)
    
    print(llista_2) #resultat ['hola']
    
Les llistes treballent molt bé juntament amb variables de tipus comptador que guardin
un valor que va canviant en el temps. 

i.e: counter = 0 #inicialitzem un comptador
    list_3 = [1,2,3,4,5]
    
    for item in list_3:
        if not item % 2:   #el % és l'operació mòdul. Aquesta línea dona els nombres parells
            counter += item
            
    print(counter)

"""

# Exercici 1

"""Fes una llista que contingui números del 1 al 25. Pots fer-ho amb la funció range
dels loops for i la funció append(), amb una list comprehension o com tu vulguis.
"""

list_ex1 = [x for x in range(1, 26)]

list_ex1_prima = []
for x in range(1, 26):
    list_ex1_prima.append(x)


# Exercici 2

"""Fes una llista amb N elements (els que vulguis) i fes servir un loop for per iterar sobre tots ells.
Per cada element, fes que s'imprimeixi per pantalla amb la funció print(). Per iterar sobre
una llista amb un for loop, fem servir la sintaxi "for item in list:"
"""

list_2 = [1, 2, 3]

for item in list_2:
    print(item)


# Exercici 3

"""Fes una funció o programa que donada una llista et sumi tots els seus elements. Pots
fer servir un for loop i l'ajut d'una variable "counter" que vagi emmagatzemant el valor
final de la suma.
"""

list_3 = [x for x in range(9)]
counter = 0
for item in list_3:
    counter += item


# Exercici 4

"""Fes una llista que retorni el nombre més gran d'una llista de nombres enters
"""

# Exercici 5

"""Fes una llista de strings. 
i.e: lst_str = ["plusquamperfet", "elefant", "plenitud", "isomer"]
i fes que l'ordinador imprimeixi per pantalla la string més llarga.

PISTA: el mètode (o funció) len() ens ajuda a saber la longitud d'una llista.
Curiosament, les strings a python són iterables, lo qual les converteix quasi bé en llistes
a efectes pràctics. 

i.e: print(len(lst_str[2])) #impimeix el número de caràcters (longitud) de la string a la posició 2
    #resultat: 8 (plenitud té 8 lletres)
"""
# Exercici 6

"""Fes una funció que, donada una llista, et vagi el·liminant tots els seus elements a 
mesura que va iterant sobre ella.

PISTA: Mira què fa la funció pop() que actua sobre llistes. 
"""

# Exercici 7

"""Fes una funció que iteri sobre una llista de nombres enters i imprimeixi "True" 
si la llista conté dos o més elements iguals.

PISTA: et pot ajudar fer servir els condicionals if, else.

i.e: lst = [1,1,3,3,4,6,7] #True
    lst2 = [1,2,3,4,5,6] #False
"""
