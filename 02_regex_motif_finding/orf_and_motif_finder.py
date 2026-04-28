#1

import re

# Regex: ORF starts with ATG, followed by 10–50 bases, ending with a stop codon (TAA/TAG/TGA)

syngene="ATGCGTACGTTAGCGGATCCGATGAAACGTTTACGCGCGATGCTAGCTAGCGTAGCTAGCTGATCGTATGAAATTTGGGCCCTAGGATGCCCTAAATGCGTACGTAGCTAGCTAAATGAAACCCGGGTTTAAATGCGCGCGTATATATATGCGCGCGTTAGATGAAAGGGCCCATTGATGCTGCTGCTTAAATGCGTGAATGAAATGCGTACGTAGCGTAGCGTAGCTAGCGTAAATGCGCGCGCGCGCGTGAATGACCCCGGGTTTAAATGTTTAAACCCGGGATGTAGATGCCCCCTGAATGCGTACGTTAGCGTAAATGCGTACGTAGCTGATCGATCGCGCGCGCGCGTTTAAATGAAATGAAAAATAGATGCCCTAAATGTGAATGCGTGA"
matchy= list(re.finditer(r"ATG[ATGC]{10,50}(TAA|TAG|TGA)", syngene))

print("ORF present", len(matchy))
for m in matchy:
    print("ORF:", m.group(), "at", m.start(), "-", m.end())
    
#ORF present 7
#ORF: ATGCGTACGTTAGCGGATCCGATGAAACGTTTACGCGCGATGCTAGCTAGCGTAG at 0 - 55
#ORF: ATGAAATTTGGGCCCTAGGATGCCCTAAATGCGTACGTAGCTAGCTAAATGA at 67 - 119
#ORF: ATGCGCGCGTATATATATGCGCGCGTTAGATGAAAGGGCCCATTGA at 132 - 178
#ORF: ATGCGTGAATGAAATGCGTACGTAGCGTAGCGTAGCTAGCGTAA at 191 - 235
#ORF: ATGCGCGCGCGCGCGTGAATGACCCCGGGTTTAAATGTTTAAACCCGGGATGTAG at 235 - 290
#ORF: ATGCCCCCTGAATGCGTACGTTAGCGTAAATGCGTACGTAGCTGA at 290 - 335
#ORF: ATGAAATGAAAAATAGATGCCCTAAATGTGAATGCGTGA at 357 - 396

#2

# Regex: N followed by any amino acid, then S/T, then any amino acid

prot="MKTLLILAVVALLAVFATDIPQGNGNQNTNTSTYNGSNTKTGQNGNSTSTNGSNTT"
matchy1= re.search(r"N.[ST].", prot)
if matchy1:
    print("N-glycosylation motif  present", matchy1.group())
else:
    print("N-glycosylation motif absent")

#N-glycosylation motif  present NTST


#3

# Regex: classical C2H2 zinc finger motif (Cys2-His2 with defined spacing)

matchy2= re.search(r"C.{2,4}C.{12}H.{3,5}H", prot)
if matchy2:
    print("Zn Finger motif present", matchy2.group())
else:
    print("Zn Finger motif absent")

#Zn Finger motif absent


#4

with open("puc18.txt", 'r') as f:
    df=f.read()

# Regex: (a|t)a(t|g)aat matches TATAAT-like promoter

matchy3= re.search(r"(a|t)a(t|g)aat", df, re.IGNORECASE)

if matchy3:
    print("promoter seq present", matchy3.group())
else:
    print("promoter seq absent")

#promoter seq present tataat 
