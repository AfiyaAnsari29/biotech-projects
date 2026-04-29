#1

def dnacom(dnaseq):
#Converting input sequence to uppercase
    dnaseq=dnaseq.upper()
    
#Replacing input sequence's bases to temporary markers    
    aa=dnaseq.replace("A", "t")
    tt=aa.replace("T", "a")
    gg=tt.replace("G", "c")
    cc=gg.replace("C", "g")
    
#Converting all temporary markers back to uppercase
    comp=cc.upper()

    return comp

#User input
inp=input("Please enter dna seq: ")
ans=dnacom(inp)
print(ans)

#Tests
assert dnacom("ATGC") == "TACG"
assert dnacom("AATTGGCC") == "TTAACCGG"
assert dnacom("GGGCCC") == "CCCGGG"


#2

def calculate_bmi(w,h):
#Applying Formula
    bmi=w/(h**2)
    return round(bmi, 2)

#User input
w=float(input("Enter weight in kg: "))
h=float(input("Enter height in m: "))
ans=calculate_bmi(w,h)
print(ans)

#Tests
assert round(calculate_bmi(70, 1.75), 2) == 22.86
assert round(calculate_bmi(50, 1.6), 2) == 19.53


#3

def count_nucleotides(dna_sequence):
#Converting input sequence to uppercase
    dna_sequence=dna_sequence.upper()

#Counting input sequence's bases    
    A=dna_sequence.count("A")
    T=dna_sequence.count("T")
    G=dna_sequence.count("G")
    C=dna_sequence.count("C")
    
    count={"A":A, "T":T, "G":G, "C":C}
    
    return count

#User input
dna_sequence=input("Please enter dna seq: ")
ans=count_nucleotides(dna_sequence)
print(ans)

#Tests
assert count_nucleotides("ATGCTTCGA") == {"A": 2, "T": 3, "G": 2, "C": 2}
assert count_nucleotides("CCGGTA") == {"A": 1, "T": 1, "G": 2, "C": 2}

