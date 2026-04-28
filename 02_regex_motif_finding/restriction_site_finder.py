import re

#Open and read the DNA sequence file

with open("puc18.txt", 'r') as fil:   
    df = fil.read().lower()           #Lowercase for consistent matching

#Dictionary of enzyme names and recognition sites
    
enzymes = {
    "EcoR1":   r"gaattc",
    "BamH1":   r"ggatcc",
    "AluI":    r"agct",
    "HindIII": r"aagctt",
    "AclI":    r"aacgtt",
    "MwoI":    r"gc[n]{7}gc"   
}

#Loop through enzymes and check for sites

for name, pattern in enzymes.items():
    matches = list(re.finditer(pattern, df))
    if matches:
        print(f"{name} site found at positions:")
        for m in matches:
            print(f"Start: {m.start()}, End: {m.end()}")
    else:
        print(f"{name} site not found")
