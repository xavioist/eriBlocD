# Ex_1

""" Crea una classe Vehicle i dóna-li els següents atributs (pots triar els noms dels atributs):
- Tipus de vehicle 
- Marca
- Model
- Any de fabricació (o Edat del vehicle)
- Estat (Nou/seminou/2a ma)
- Data última ITV

Després, crea un mètode que et permeti saber quan li tocarà al vehicle la pròxima ITV. 
Tindrem en compte que un vehicle de menys de 4 anys ha de passar la ITV cada 4 anys,
un vehicle de més de 4 anys l'ha de passar cada 2 i un vehicle amb més de 10 anys l'ha de passar cada any.

Comprova amb tres exemples que la classe funciona.

NOTA: Python inclou el mòdul datetime (import datetime) que té la funció datetime(yyyy,mm,dd) , que et permet treballar còmodament amb dates.

DOCUMENTACIÓ: 
https://www.w3schools.com/python/python_datetime.asp
https://docs.python.org/3/library/datetime.html 
"""

# Ex 2

""" Fes una classe que es digui Gos (o Gat) i que tingui els atributs (tu decideixes els noms dels atributs):
- nom
- tamany
- raça (Per defecte, "desconeguda")
- data de naixement (fes servir el mòdul datetime)

I que tingui els mètodes següents:

- bordar (o miolar): El gos o gat ha de bordar o miolar (imprimir per pantalla "bup" o "miau")
- obtenir_nom: T'ha de retornar el nom de l'animal
- canviar_nom: Et permet canviar el nom a l'animal
- anys_relatius: T'ha de donar els anys de l'animal en el seu sistema de referència:
    * 1 any de gos = 7 anys de persona (aprox)
    * 1 any de gat = 5 anys de persona (aprox)
    
DOCUMENTACIÓ: 
https://www.w3schools.com/python/python_datetime.asp
https://docs.python.org/3/library/datetime.html 

"""


# Ex 3

"""  Fes una classe que es digui Carta i que tingui els atributs següents (tu tries el nom que fiques als atributs):
- pal (piques, cors, trèbols o diamants)
- valor (As, 2, 3, ..., J, Q, K)

I una altra classe anomenada Deck amb els següents atributs:

- pack: s'ha d'inicialitzar amb una llista plena d'objectes de la classe Carta
- descartes: s'ha d'inicialitzar amb una llista buida

Que ha de tenir els següents mètodes:
- pick: retorna una carta de la part superior del deck (la primera o l'última)
- barrejar: canvia l'ordre de les cartes del deck

Per comprovar que funciona, intenta robar 6 cartes, mira la carta de la part superior de la biblioteca,
barreja, i roba una més.
"""
