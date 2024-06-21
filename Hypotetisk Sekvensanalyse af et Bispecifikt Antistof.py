from Bio.SeqUtils.ProtParam import ProteinAnalysis

# Hypotetisk sekvens af et bispecifikt antistof, der binder til CD20 og CD3
sequence_str_cd20 = "EVQLVESGGGLVQPGGSLRLSCAASGFTFSSYAMSWVRQAPGKGLEWVSAISYDGSTYYADSVKGRFTISRDNAKNTLYLQMNSLRAEDTAVYYCARGGGGMDVWGQGTTVTVSS"
sequence_str_cd3 = "QVQLVQSGAEVKKPGSSVKVSCKASGDTFAYWMNWVRQAPGQGLEWIGYINPSRGYTNYNQKFKGKATLTADKSSSTAYMQLSSLKTSEDTAVYYCARERDGWGQGTTVTVSS"

# Kombiner sekvenserne til et bispecifikt antistof (for enkelheds skyld)
sequence_str = sequence_str_cd20 + sequence_str_cd3
print(f"Aminosyresekvens: {sequence_str}")

# Analyser sekvensen
protein_analysis = ProteinAnalysis(sequence_str)

# Beregn basiske egenskaber
molecular_weight = protein_analysis.molecular_weight()
aromaticity = protein_analysis.aromaticity()
instability_index = protein_analysis.instability_index()
isoelectric_point = protein_analysis.isoelectric_point()
secondary_structure_fraction = protein_analysis.secondary_structure_fraction()

# Udskriv resultater
print(f"Molekylvægt: {molecular_weight}")
print(f"Aromatisk indeks: {aromaticity}")
print(f"Instabilitetsindeks: {instability_index}")
print(f"Isoelectric punkt: {isoelectric_point}")
print(f"Andel af sekundær struktur (helix, turn, sheet): {secondary_structure_fraction}")
