""" Introducció als diccionaris

Els diccionaris de python són estructures de dades ordenades que s'utilitzen per a 
emmagatzemar informació en parells de key:value. Cada element que hi guardem té associada
una clau que es fa servir per accedir al valor. La seva sintaxi és diferent a la de les
llistes per tal de poder diferenciar-les. Cada parell de clau:valor és únic!

i.e: dict_prova = {
    "marca": "Renault",
    "model": "Clio",
     "any": 1996,
     "colors":['blau','vermell','blanc']
    }
    
    dict_prova["marca"] #retorna el valor "Renault"
    dict_prova["colors"][1] #retorna "vermell"
    
Els mètodes associats als diccionaris els podeu trobar a:
    https://www.w3schools.com/python/python_ref_dictionary.asp
    
Els diccionaris també són iterables. Es poden iterar per claus, valors o les dues coses.
Farem servir els mètodes values(), keys() i items()

i.e: 

    for i in dict_prova:
        print(dict_prova[i]) #retorna els valors del diccionari
        
    for i in dict_prova.values():
        print(i) #fa el mateix que l'anterior. Retorna els valors del diccionari
        
    for i in dict_prova.keys():
        print(i) #retorna les claus del diccionari
        
    for i in dict_prova.items():
        print(i) #retorna un tuple dels parells key:value
        
    for i, j in dict_prova.items():
        print(i, j) #retorna claus i valors per separat
        
Els diccionaris, igual que les llistes, es poden "anidar" (nested dictionaries, nested lists)
Això significa que es poden posar diccionaris dintre de diccionaris.

i.e: dict_nested = {
    "animal_1":{"nom":"Altramuz",
                "especie":"Gos",
                "good_boy":True},
    "animal_2":{"nom":"Petunia",
                "especie":"Oca",
                "good_boy":False},
    "animal_3":{"nom": "Alpha",
                "especie":"gos",
                "color":['negre','taronja','blanc'],
                "good_boy":True}
}

Accedim als seus valors de la següent manera:

    dict_nested["animal_1"]["nom"] #retorna "Altramuz"
    dict_nested["animal_2"]["good_boy"] #retorna False
    dict_nested["animal_3"]["color"][0] #retorna "negre"
     
Els diccionaris són especialment útils quan treballem amb variables complexes i ens
ajuden a que el nostre codi sigui més llegible.
"""

# Exercici 1

""" Fes un diccionari que sigui la fitxa d'un alumne de la uni: Nom, NIU, edat,
email, direcció i telefon.
"""

# Exercici 2

""" Amb el diccionari de l'exercici 1, canvia el valor del número de telèfon i el NIU
de l'estudiant fent servir un dels mètodes propis dels diccionaris. (https://www.w3schools.com/python/python_ref_dictionary.asp)
"""

# Exercici 3

""" Fes un diccionari anidat que contingui les fitxes de tres alumnes amb les mateixes
claus que a l'exercici 1.
"""

# Exercici 4

""" Fes un programa que et permeti iterar sobre les claus i valors un diccionari de python mitjançant un loop for. 
PISTA: volem iterar sobre les claus i sobre els valors, per tant necessitarem dos iteradors. Un diccionari en sí mateix no és iterable,
així que necessitem obtenir els seus ITEMS amb una funció pròpia. i.e:

for key, value in ...
"""
