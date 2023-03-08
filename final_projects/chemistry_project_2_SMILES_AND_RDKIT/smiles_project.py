from rdkit import Chem
from rdkit.Chem import Draw
from rdkit.Chem.Draw import IPythonConsole

IPythonConsole.drawOptions.addAtomIndices = True
IPythonConsole.drawOptions.addStereoAnnotation = False
IPythonConsole.molSize = 200, 200


def mol_with_atom_index(mol):
    for atom in mol.GetAtoms():
        atom.SetAtomMapNum(atom.GetIdx())
        print(atom.GetIdx())
        print(atom.GetSymbol())
    return mol


mysmiles = ["[H][H]", "O=C=O", "COC"]
mymols = []

for el in mysmiles:
    molec = Chem.MolFromSmiles(el)
    mymols.append(molec)

print(mymols)

m = Chem.MolFromSmiles("C([C@@H]1[C@H]([C@@H]([C@H](C(O1)O)O)O)O)O")  # non-canonic

m2 = Chem.MolFromSmiles("C(C1C(C(C(C(O1)O)O)O)O)O")  # canonic
mol_with_atom_index(m)

print(
    Chem.FindMolChiralCenters(
        m, force=True, includeUnassigned=True, useLegacyImplementation=True
    )
)

Chem.Draw.MolToFile(m, "/home/xavi/Desktop/glucose.png")
