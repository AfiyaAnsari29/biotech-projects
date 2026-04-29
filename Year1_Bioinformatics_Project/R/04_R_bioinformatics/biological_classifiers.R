# Set your working directory to the folder containing this script
# Session > Set Working Directory > To Source File Location

#1: Classify Organisms by Size
x = c(10,14,16,26,56,89,6)
for(i in x){
  if(i < 10){
    print("organism is small")       #Less than 10  small
  } else if(i >= 10 && i <= 50){
    print("organism is medium")      #Between 10 and 50  medium
  } else {
    print("organism is large")       #Greater than 50  large
  }
}

#2: Growth rates
r1 = 1.5
r2 = 1.2
if(r1 > r2){
  print("Strain 1 grows faster")     #Compare growth rates
} else if(r2 > r1){
  print("Strain 2 grows faster")
} else {
  print("Both strains grow at the same time")
}

#3: Gene expression level
gene = c(5, 12, 7, 15, 3, 20)
for(i in gene){
  if(i > 7){
    print(i)                         #Print only values greater than 7
  }
}
subset(gene, gene > 7)

#4: Categorize Animals by Weight
weight = c(25, 75, 180, 250, 40)
for(i in weight){
  if(i < 50){
    print("organism is small")       # Weight < 50 small
  } else if(i >= 50 && i <= 200){
    print("organism is medium")      # 50–200 medium
  } else {
    print("organism is large")       # >200 large
  }
}

#5: Count Occurrences of a Specific Amino Acid
prot = c("A", "L", "V", "L", "G", "L")
count = 0
for(i in prot){
  if(i == "L"){
    count = count + 1                #Increment count when amino acid is "L"
  }
}
print(count)                         #Print total count of "L"
