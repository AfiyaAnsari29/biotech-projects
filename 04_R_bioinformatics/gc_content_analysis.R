# Set your working directory to the folder containing this script
# Session > Set Working Directory > To Source File Location

library(seqinr)   #For sequence analysis functions (e.g., s2c, GC)
library(stringr)  #For string operations (e.g., str_count, str_length)

#1:Identify coding sequences (start with ATG)

seq1= c("ATGCTC","GGTGCG","TGTTTCG","ATGTTCG","GGCCTGC","TTCGCGTAT","ATGGGTCT")
for (i in seq_along(seq1)) {
  if (startsWith(seq1[i], "ATG")) {
    cat(i, "is coding sequence\n")   #Print index if sequence starts with ATG
  }
}

#2:Check sequence length

seq2= "ATGGGCTGCGTGCATTGCGTACTGGGTCCCAATGGCGGGTTCCAAAGGGGTCGATGACGTGCCGTAA"
if(nchar(seq2) > 30){
  print("seq is too long")           #Flag if sequence length > 30
} else {
  print(seq2)
}

#3:Filter accession codes starting with 'a' and ending with '4'

acc= c("ab56","bh84","hv76","ay93","ap97","bd72")
ans= acc[startsWith(acc,"a") & endsWith(acc,"4")]
print(ans)

#4:GC content calculation
seq3= s2c("ATGGTGGTGATGTAGTAGCCCAGATGATCCAGTACAGTAGG")   #Convert string to vector of bases
gc_content= GC(seq3)                                   #GC fraction
gc_content1= gc_content*100                          #Convert to percentage
print(gc_content1)

#5:Create dataframe and calculate GC content for each sequence
acc= c("ab56","bh84","hv76","ay93","ap97","bd72")
seq5= c("ggtcgtgagtgac","aactcgtagatgacg","agctgcgttgat",
         "agtgacgtcatgacg","acgtgtcagtgac","tgacgtgacgtaa")
df1= data.frame(acc, seq5)
print(df1)

#Calculate GC percentage for each sequence

a= str_count(tolower(df1$seq5), "[gc]")       #Count G or C bases
b= str_length(df1$seq5)              #Sequence length
perc= a*100/b                    #GC percentage
df1= cbind(df1, perc)
print(df1)

#Loop to classify sequences as GC-rich or AT-rich

for(i in 1:length(perc)){
  if(perc[i] > 50){
    print("percent: seq is GC rich")
  }else{
    print("percent: seq is AT rich")
  }
}
