# Assignment 3: Web Scraping (amb Beautiful Soup)

Documentation:
- https://victormurcia-53351.medium.com/extracting-thermodynamic-properties-from-the-nist-chemistry-webbook-using-python-4008bd9736c3
- https://realpython.com/python-web-scraping-practical-introduction/


1. Una query és una petició d'informació que es realitza generalment sobre pàgines web. Python ens permet comunicar-nos amb pàgines web i obtenir informació que estigui gaurdada online per a fer-la servir en els nostres programes. Una part molt important de les queries són les expressions regulars (RegEx o Regular Expressions). Busca informació sobre què són les regular expressions i explica perquè es fan servir. Explica també com estan integrades a Python. PISTA: Hi ha un mòdul específic de Python que conté regular expressions. Busca informació també sobre què són els codis HEX i el ASCII i per què es fan servir en programació.

2. Expliqueu amb les vostres paraules què fa el codi, bloc per bloc. 

3. El codi tal i com s'ha entregat està incomplert i no funciona correctament. Quan fem la query ens retorna un dataframe buit tot i que el programa és capaç d'obtenir els valors que li hem demanat:

Empty DataFrame
Columns: [Quantity, Value, Units]
Index: []

Modifica el final del codi per a que retorni un dataframe amb els valors corresponents. PISTA: Tingueu en compte que la funció retorna "df". Aquest és el dataframe que ha de contenir la informació.

4. Python ens permet executar programes que fem com si fossin scripts amb la instrucció a final de programa:

if __name__ == "__main__":
    linea 1
    linea 2 
    ...
    return

Això vol dir que podem escriure vàries funcions i, segons el que ens convingui, fer-les servir d'una manera o d'una altra.
Busqueu informació de com funciona aquesta intrucció (aquí per exemple https://realpython.com/if-name-main-python/). Modifiqueu el programa per a que faci queries de 10 elements diferents i guardi en un diccionari el nom de l'element i la seva entalpia de formació. 

