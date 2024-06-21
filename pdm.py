from Bio.PDB import PDBParser, PDBIO, PPBuilder
import matplotlib.pyplot as plt

# Hent en proteinstruktur fra PDB
pdb_id = "1TUP"
pdb_filename = "C:\\Users\\tom.zbc\\PycharmProjects\\Proteindesignandmodelling\\1TUP.pdb"

# Parse PDB-filen
parser = PDBParser()
structure = parser.get_structure(pdb_id, pdb_filename)

# Ekstrahere sekvensen af det første polypeptid
ppb = PPBuilder()
for pp in ppb.build_peptides(structure):
    sequence = pp.get_sequence()
    print(sequence)

# Visualisering af proteinstruktur
# (Simpel visualisering af alpha-carbon backbone)
def plot_protein_structure(structure):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    for model in structure:
        for chain in model:
            for residue in chain:
                for atom in residue:
                    if atom.get_id() == "CA":  # Alpha carbon
                        coord = atom.get_coord()
                        ax.scatter(coord[0], coord[1], coord[2], c='b', marker='o')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.show()

plot_protein_structure(structure)
