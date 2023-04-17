# Assignment 2 SMILES & RDKIT

1. RDKIT és una API que ens permet treballar amb molècules i estructures químiques complexes de manera senzilla. RDKIT utilitza tota una sèrie de classes per tal de representar acuradament les propietats i característiques de les molècules. Això ens permet calcular paràmetres, generar i optimitzar estructures moleculars, visualitzar molècules, etc. RDKIT utilitza com a fitxer de partida el d'una estructura molecular en forma de coordenades 3D (pot ser un pdb, mol, xyz, etc...) que es pot trobar al PDB Databank o es pot generar per altres mitjans. Alternativament, pot acceptar codis SMILES per a molècules no massa grans.

Busqueu informació sobre els codis SMILES: què són, com funcionen i per a què són útils en el context de la química computacional? Feu una funció que, donada una llista amb SMILES, ens permeti generar un conjunt de molècules de RDKIT.

2. En aquesta pàgina trobareu documentació de RDKIT on es fa servir el codi SMILES per a generar les estructures moleculars de partida. (https://www.rdkit.org/docs/Cookbook.html). Busqueu el codi SMILES (SMILES canònic) de la glucosa i genereu un objecte "mol" de RDKIT a partir del seu SMILES. Un cop el tingueu, feu un programa que us permeti identificar els seus centres quirals. Quants centres quirals té? A què es deu aquest resultat? Agafeu ara el SMILES de la beta-D-glucopiranosa i compareu-los.

3. RDKIT ens permet iterar sobre tots els àtoms d'una molècula. Per cada àtom de la glucosa de l'exercici anterior, troba la manera d'iterar sobre els seus àtoms i obtenir el símbol del seu element i el índex de cadascún d'ells. Un cop estiguis, guarda la teva molècula en forma de fitxer PDB.

4. L'avantatge dels codis SMILES és que són strings. Fent servir RDKIT, tria 5 codis smiles de diferents molècules i fes un programa que:

- Calculi les càrregues Gasteiger de cada àtom de la molècula (càrregues elèctriques parcials).
- Guardi la molècula en format .mol.

5. Torna a escriure el programa amb pseudocodi i comenta què fa cada apartat del programa
