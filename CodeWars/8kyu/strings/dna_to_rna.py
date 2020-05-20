# Convert DNA to RNA string 
# Inputs = ATGC 
# In rna, T becomes U 

def dna_to_rna(DNA):
  return DNA.replace("T", "U")

print(dna_to_rna("TTTT")) # UUUU
print(dna_to_rna("ATCG")) # AUCG
print(dna_to_rna("GACC")) # GACC