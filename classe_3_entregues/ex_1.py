# Exercici 1
""" Fes una classe que s'anomeni Atom i tingui les següents propietats:
- Pes molecular (float)
- Simbol de l'element (string)
- Nombre atòmic (int)
- Classificació a la taula periòdica (string) (gas noble, lantànid, alcalí, etc...)
- Coordenades a l'espai (list[float]) [poseu unes coordenades qualsevols]

I que inclogui els mètodes següents:

- Un mètode que es digui compare_atoms() i et digui quin dels dos àtoms té
un pes molecular major

- Un mètode que retorni True si l'àtom és un gas noble i False si no ho és

- Un mètode que et retorni la distància entre dos àtoms
"""

# Exercici 2
""" Prenent de referència la classe Atom que s'ha fet, afegeix-hi un mètode que
agafi dos àtoms i una taula de distàncies i, segons la seva distància, et digui si poden estar enllaçats o no.
COMPTE! Un àtom de carboni i un àtom d'hel·li mai podran estar enllaçats per molt junts
que estiguin, i això el programa ho ha de tenir en compte.

PISTA: Pots generar una taula amb distàncies d'enllaç típiques entre atoms.
Pren de referència la imatge taula_bond_distance.png i inclou només les 
distàncies on estigui involucrat l'àtom de carboni. La taula (llista, tuple o diccionari) conté
distàncies d'enllaç per parells d'àtoms.

Un cop s'ha calculat la distància entre àtoms,retorna true si poden estar enllaçats i false
en el cas contrari.

(si dist_atoms < dist_enllaç -> possible)
"""


class Atom:
    def __init__(self, molec_weight, symbol, atomic_num, periodic, coords):
        self.molec_weight = molec_weight
        self.symbol = symbol
        self.atomic_num = atomic_num
        self.periodic = periodic
        self.coords = coords

    def compare_atoms(self, atom2):
        if self.molec_weight > atom2.molec_weight:
            print(self.symbol, " weights more")
        else:
            print(atom2.symbol, " weights more")

    def is_noble(self):
        if self.periodic == "Noble Gas":
            return True
        else:
            return False

    def distance(self, atom2):
        import numpy as np

        d = [(self.coords[i] - atom2.coords[i]) ** 2 for i in range(0, 3)]
        return np.sqrt(sum(d))

    def is_bond_possible(self, atom2, table):
        dist = self.distance(atom2)
        sym_1 = self.symbol
        sym_2 = atom2.symbol

        if (self.symbol or atom2.symbol) in "He Ne Ar Kr Xe Rn":
            print("Cannot form bond with noble gas!")
            return False

        for t in table:
            if sym_1 and sym_2 in t:
                if dist <= t[2]:
                    print(
                        "can be bonded, dist",
                        dist,
                        "is smaller than bond_dist = ",
                        t[2],
                    )
                    return True
                else:
                    print(
                        "cannot be bonded, dist",
                        dist,
                        "is greater than bond_dist = ",
                        t[2],
                    )
                    return False


table = [("C", "C", 1.54), ("C", "O", 1.43)]

carboni = Atom(12.011, "C", 12, "Non Metal", [2, 2, 0])
oxigen = Atom(15.999, "O", 16, "Non Metal", [1, 0, 1])

carboni.is_bond_possible(oxigen, table)
