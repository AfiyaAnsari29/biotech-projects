# Set your working directory to the folder containing this script
# Session > Set Working Directory > To Source File Location

#a: Making vectors
f= c(71.0, 77.3, 82.6, 96.1, 106.6, 112.8, 121.2, 126.4, 127.5, 143.1)   #Feeding dive O2 consumption
nf= c(42.2, 51.7, 59.8, 66.5, 81.9, 82.0, 81.3, 81.3, 96.0, 104.1)       #Non-feeding dive O2 consumption
length(f)      #Number of feeding dives
length(nf)     #Number of non-feeding dives

#b: Difference in oxygen consumption
DiffO2= f-nf   #Element-wise difference between feeding and non-feeding dives

#c: Average difference between feeding and non-feeding dives
f.mean= mean(f)          #Mean O2 consumption for feeding dives
nf.mean= mean(nf)        #Mean O2 consumption for non-feeding dives
avgdiff= f.mean - nf.mean
print(avgdiff)
cat("The average difference between feed dive and non-feed dive is", avgdiff)

#d: Ratio of O2 consumption
vec1= f / nf             #Element-wise ratio of feeding to non-feeding
print(vec1)

#e: Log of the ratios
ln = log(vec1)            #Natural log of ratios
print(ln)
mean.ln= mean(ln)        #Mean of log ratios
print(mean.ln)

#f: Replacing the entry
f[2]= 80.4               #Replace 2nd feeding dive value
nf[2]= 56.7              #Replace 2nd non-feeding dive value

#g: Subset of values for animals 5–10
new.f = f[5:10]           #Feeding dives 5–10
print(new.f)
new.nf = nf[5:10]         #Non-feeding dives 5–10
print(new.nf)
