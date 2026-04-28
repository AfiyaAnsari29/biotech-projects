# Read the DNA sequence
with open("genomic_DNA.txt", 'r') as fil:
    dna_seq = fil.read()

# Extract exons and intron
exon1= dna_seq[0:63]
exon2= dna_seq[63:91]
intron= dna_seq[91:]

# Combine exons to simulate spliced mRNA
coding_seq= exon1+exon2

# Save the spliced coding sequence
with open("coding_sequence.txt", 'w') as f:
    f.write(coding_seq)

# Print results
print("Exon 1:", exon1)
print("Exon 2:", exon2)
print("Intron:", intron)
print("Spliced coding sequence (mRNA):", coding_seq)




