#1
s1=set(("BRCA1","TP53","EGFR","BRCA1","MYC","TP53"))
print(s1)

#2
#genes in sample A
sA= set(("TP53", "BRCA1", "MYC", "PTEN"))
#genes in sample B
sB= set(("BRCA1", "EGFR", "PTEN", "AKT1"))

#genes common to both samples
inter=sA.intersection(sB)
print(inter)

#genes only in sample A
diff=sA.difference(sB)
print(diff)

#all genes from both samples
uni=sA.union(sB)
print(uni)

#3
gene={"TP53":"Tumor suppressor",
      "EGFR":"Cell signaling",
      "MYC":"Transcription factor"}

k=gene.keys()   #get all gene names
v=gene.values() #get all functions
print(gene)     #print whole dictionary
print(k)        #print keys
print(v)        #print values


#4
#dictionary of codons and amino acids
aa={
    "AUG" : "Methionine",
    "UUU" : "Phenylalanine",
    "UUC" : "Phenylalanine",
    "UAA" : "Stop"
    }

print(aa)
st=aa.get("AUG")
print(st)


#5
gene_expression= {"TP53": 12.5, "BRCA1": 8.2, "MYC": 15.6, "EGFR": 6.1}

#Gene with highest expression
highest_gene = max(gene_expression, key=gene_expression.get)

#Gene with lowest expression
lowest_gene = min(gene_expression, key=gene_expression.get)

#Printing the results
print(highest_gene, "=", gene_expression[highest_gene])
print(lowest_gene, "=", gene_expression[lowest_gene])
