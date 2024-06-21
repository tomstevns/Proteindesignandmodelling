import os

# Hent en proteinstruktur fra PDB
# Test
pdb_id = "1TUP"
pdb_filename = "C:\\Users\\tom.zbc\\PycharmProjects\\Proteindesignandmodelling\\1TUP.pdb"

# Kontrollér om filen eksisterer
if os.path.exists(pdb_filename):
    print("Filen findes.")
else:
    print("Filen findes ikke:", pdb_filename)
