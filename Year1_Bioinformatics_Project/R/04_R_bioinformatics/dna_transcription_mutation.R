# Set your working directory to the folder containing this script
# Session > Set Working Directory > To Source File Location

library(seqinr)   #For DNA sequence utilities (s2c, GC, etc.)
library(stringr)  #For string manipulation (str_replace_all, str_sub, etc.)

#1: DNA to RNA (transcription)

dna= s2c("ATGCGTGACGTCCAATTGGACGATGACGATG")
#Note: transcribe() is from Biostrings, not seqinr so in seqinr, you can manually replace T with U.
rna= str_replace_all(paste(dna, collapse=""), "T", "U")   # Convert DNA string to RNA string
print(rna)

#2:Extract exons and build coding sequence

dna2= "ATGAGAGGACAGTAGCAAAGATCAGTAGAAGCAGGCACGAGCTAGCAGTAGCGATAGCAGTAGCAGTAGCGATAGCGATGACAGATAGCAGTAGCAGTGACAG"
e1= str_sub(dna2, 1, 33)                     #First exon
e2= str_sub(dna2, 75, nchar(dna2))           #Second exon
coding_seq= paste0(e1, e2)                   #Concatenate exons
cat("Coding sequence:\n", coding_seq, "\n")

#3:Restriction site location and fragmenting

dna3= dna2
rsite= "GGCACG"
pos= str_locate(dna3, rsite)                 #Locate restriction site
print(pos)
f1= str_sub(dna3, 1, pos[1]-1)               #Fragment before site
f2= str_sub(dna3, pos[1], nchar(dna3))       #Fragment including site onward
print(f1)
print(f2)

#4:Mutation function (replace base at given position with a random alternative)

mutate_dna_stringr = function(dna_seq, position) { 
  nucleotides <- c("A", "T", "C", "G")
  current = str_sub(dna_seq, position, position) 
  new_base = sample(setdiff(nucleotides, current), 1) 
  str_sub(dna_seq, position, position) = new_base 
  return(dna_seq) 
}
set.seed(123) 
mutate_dna_stringr("ATCGTA", 3)
